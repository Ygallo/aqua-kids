from django.shortcuts import render
from django.views import generic, View
from courses.models import Course, Category

# Create your views here.


def Home(request):
    """View to return swimschool courses, sorting and queries"""

    course_categories = Category.objects.all()

    context = {
        'course_categories': course_categories,
    }

    return render(request, 'index.html', context)


def timetable(request):
    """View to return the timetable"""
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'timetable.html', context)


def about_us(request):
    """View to return the timetable"""
    return render(request, 'about_us.html')


def contact_us(request):
    """View to return the timetable"""
    return render(request, 'contact_us.html')


def contact_success(request):
    """View to return succes on contact form """
    return render(request, 'contact_success.html')
