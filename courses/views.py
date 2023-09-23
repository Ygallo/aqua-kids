from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from . models import Course, Category

from .forms import CourseForm

# Create your views here.


def course_categories(request):
    """View to return swimschool courses, sorting and queries"""

    course_categories = Category.objects.all()

    context = {
        'course_categories': course_categories,
    }

    return render(request, 'courses/course_categories.html', context)


def all_courses(request):
    """View to return all swim courses"""

    courses = Course.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        courses = courses.filter(category__course_type__in=categories)
        # categories = Category.objects.filter(name__in=categories)

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('course'))
          
        queries = Q(level__icontains=query) | Q(description__icontains=query)
        courses = courses.filter(queries)

    context = {
        'courses': courses,
        'search_term': query,
    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    """ A view to show individual course details """

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_detail.html', context)


def add_course(request):
    """ Admin can add a course to the swim school"""
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course added successfully!')
            return redirect(reverse('course_detail', args=[course.id]))
        else:
            messages.error(request, 'Failed to add the course. Please make sure the form is valid.')
    else:
        form = CourseForm()

    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_course(request, course_id):
    """ Admin can edit a course to the swim school"""
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully!')
            return redirect(reverse('course_detail', args=[course_id]))
        else:
            messages.error(request, 'Failed to update the course. Please make sure the form is valid.')
    else:
        form = CourseForm(instance=course)
        messages.info(request, f'You are editing {course.name}')

    template = 'courses/edit_course.html'
    context = {
        'form': form,
        'course': course,
    }

    return render(request, template, context)


def delete_course(request, course_id):
    """ Admin can delete a course to the swim school"""
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.success(request, 'The course has been deleted')
    return redirect(reverse('courses'))
