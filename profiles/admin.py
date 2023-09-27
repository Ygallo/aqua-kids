from django.contrib import admin
from .models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'date_of_birth',
        'gender',
        'level',
        'guardian',
        'special_requirements',
    )


admin.site.register(Student, StudentAdmin)
