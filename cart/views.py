from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from courses.models import Course

# Create your views here.


def view_cart(request):
    """View to return the cart contents page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add a quantity of the specific course to the shopping bag"""

    course = get_object_or_404(Course, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'You updated{course.level} quantity on your cart {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'You added {course.level} to your cart')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def adjust_cart(request, course_id):
    """Adjust the quantity of the specified course to the specified amount"""

    course = get_object_or_404(Course, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[course_id] = quantity
        messages.success(
            request, f'You updated{course.level} quantity on your cart {cart[item_id]}')
    else:
        cart.pop(course_id)
        messages.success(
            request, f'You removed {course.level} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, course_id):
    """Remove the item from the shopping cart"""

    try:
        course = get_object_or_404(Course, pk=course_id)
        cart = request.session.get('cart', {})

        cart.pop(course_id)
        messages.success(request, f'Remove {course.level} from your bag')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
