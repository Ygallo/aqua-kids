from django.shortcuts import render
from . models import Course

# Create your views here.


def courses(request):
    """View to return swimschool courses, sorting and queries"""

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)
