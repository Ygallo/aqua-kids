from django.contrib import admin
from .models import Category, Course, Levels

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'level',
        'category',
        'start_date',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'course_type',
        'description',
    )


class LevelsAdmin(admin.ModelAdmin):
    list_display = (
        'level',
        'who_for',
        'skills',
    )

admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Levels, LevelsAdmin)
