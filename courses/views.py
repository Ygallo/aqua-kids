from django.shortcuts import render
from . models import Course, Category

# Create your views here.


def course_categories(request):
    """View to return swimschool courses, sorting and queries"""

    course_categories = Category.objects.all()

    context = {
        'course_categories': course_categories,
    }

    return render(request, 'courses/course_categories.html', context)
