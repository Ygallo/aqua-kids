from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm, StudentForm
from .models import Order, OrderLineItem
from courses.models import Course
from profiles.forms import UserProfileForm
from profiles.models import UserProfile, Student
from cart.contexts import cart_contents

import stripe
import json
# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    context = {
        "order_form": "",
        "client_secret": "",
        "stripe_public_key": "",
        "students": "",
    }

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {}
        for key, value in request.POST.items():
            form_data[key] = value

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()

            for item_id, item_data in cart.items():
                current_student = form_data.get("student_"+item_id)
                try:
                    course = Course.objects.get(id=item_id)
                    student = Student.objects.get(id=current_student)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            course=course,
                            quantity=item_data,
                            student=student,
                        )
                        places_left = course.places - item_data
                        course.places = places_left
                        course.save()
                        order_line_item.save()

                except Course.DoesNotExist:
                    messages.error(request, (
                        "The course in your cart wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty")
            return redirect(reverse('courses'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                queryset = Student.objects.all()
                students = queryset.filter(guardian=profile.id)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                })
                context["students"] = students

            except UserProfile.DoesNotExist:
                order_form = OrderForm()

        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context['order_form'] = order_form
    context["stripe_public_key"] = stripe_public_key
    context["client_secret"] = intent.client_secret
    template = 'checkout/checkout.html'
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_email': order.email,
                'default_postcode': order.postcode,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
       Your order number is {order_number}. A confirmation \
       email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
