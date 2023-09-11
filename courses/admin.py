from django.contrib import admin
from .models import Category, Course

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'level',
        'start_date',
    )


admin.site.register(Course, CourseAdmin)
admin.site.register(Category)