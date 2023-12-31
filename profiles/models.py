from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from courses.models import Levels

# Create your models here.


class UserProfile(models.Model):
    """
    A user profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_email = models.EmailField(max_length=254, null=False, blank=False)
    default_phone_number = models.CharField(max_length=20, null=False,
                                            blank=False)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    name = models.CharField(max_length=50, default='Please add student name')
    surname = models.CharField(max_length=50, default='Add student surname')
    date_of_birth = models.DateField()

    MALE = 'MALE'
    FEMALE = 'FEMALE'
    NON_BINARY = 'NON_BINARY'
    PREFER_NOT_TO_RESPOND = 'PREFER_NOT_TO_RESPOND'
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NON_BINARY, 'Non Binary'),
        (PREFER_NOT_TO_RESPOND, 'Prefer not to respond'),
    ]
    gender = models.CharField(
        max_length=25,
        choices=GENDER,
    )
    level = models.ForeignKey(Levels, on_delete=models.CASCADE)
    special_requirements = models.TextField(max_length=200, default='')
    guardian = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='students')

    def __str__(self):
        return self.name
