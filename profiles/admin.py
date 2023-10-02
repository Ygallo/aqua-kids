from django.contrib import admin
from .models import Student, UserProfile

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


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_phone_number',
        'default_email',
    )


admin.site.register(Student, StudentAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
