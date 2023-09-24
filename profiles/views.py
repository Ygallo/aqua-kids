from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Student
from .forms import UserProfileForm, StudentForm
from checkout.models import Order

# Create your views here.


@login_required
def profile(request):
    """Display the user profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        if request.POST.get("form_type") == 'formP':
            #Handle Elements from first Form
            form = UserProfileForm(request.POST, instance=profile)
            student_form = StudentForm(instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')
            else:
                messages.error(request, 'Error on update. Make sure the form is valid.')
        elif request.POST.get("form_type") == 'formS':
            #Handle Elements from second Form
            student_form = StudentForm(request.POST, instance=profile)
            form = UserProfileForm(instance=profile)
            if student_form.is_valid():
                student_form.save()
                messages.success(request, 'Student updated successfully')
            else:
                messages.error(request, 'Error on update. Make sure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
        student_form = StudentForm(instance=profile)

   # students = profile.students.all() 
    students = profile.students.filter(id=request.user.id)  
    
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'student_form': student_form,
        'orders': orders,
        "students": students,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def student(request):
    """Display the user profile"""
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=profile)
        if student_form.is_valid():
            student_form.save()
            messages.success(request, 'Student updated successfully')
        else:
            messages.error(request, 'Error on update. Make sure the form is valid.')
    else:
        student_form = StudentForm(instance=profile)
        
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    students = profile.students.all()
    

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'student_form': student_form,
        'orders': orders,
        "students": students,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
