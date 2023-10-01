from django.shortcuts import render, get_object_or_404, redirect, reverse    
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import UserProfile, Student, User
from .forms import UserProfileForm, StudentForm
from checkout.models import Order

# Create your views here.


@login_required
def profile(request):
    """Display the user profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    queryset = Student.objects.all()
    students = queryset.filter(guardian=profile.id)

    if request.method == 'POST':
        if request.POST.get("form_type") == 'formP':
            # Handle Elements from first Form
            form = UserProfileForm(request.POST, instance=profile)
           # student_form = StudentForm()
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')
            else:
                messages.error(request, 'Error on update. Make sure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
        form = UserProfileForm()
       # student_form = StudentForm()

    # students = profile.students.all() 

    orders = profile.orders.all()

    template = 'profiles/profile.html'
  
    context = {
        'form': form,
        'orders': orders,
        'students': students,
        'current_user': profile,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def student(request):
    """Display the user profile"""
    profile = get_object_or_404(UserProfile, user=request.user)
    queryset = Student.objects.all()
    students = queryset.filter(guardian=profile.id)

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

    template = 'profiles/students.html'
    context = {
        'student_form': student_form,
        "students": students,
    }

    return render(request, template, context)


@login_required
def add_student(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Student added successfully!')
            return redirect(reverse('students'))
        else:
            messages.error(request, 'Failed to add the student. Please make sure the form is valid.')
    else:
        form = StudentForm()

    template = 'profiles/add_student.html'
    context = {
        'form': form,
        'current_user': profile,
    }

    return render(request, template, context)


@login_required
def edit_student(request, student_id):
    """ Admin can edit a course to the swim school"""
    profile = get_object_or_404(UserProfile, user=request.user)
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            # return redirect(reverse('student', args=[student_id]))
            return redirect(reverse('student'))
        else:
            messages.error(request, 'Failed to update the student. Please make sure the form is valid.')
    else:
        form = StudentForm(instance=student)
        messages.info(request, f'You are editing {student.name}')

    template = 'profiles/edit_student.html'
    context = {
        'form': form,
        'student': student,
        'current_user': profile,
    }

    return render(request, template, context)


@login_required
def delete_student(request, student_id):
    """ Delete a student from your profile """

    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    messages.success(request, 'The student was deleted!')

    template = 'profiles/delete_student.html'

    return redirect(reverse('student'))



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
