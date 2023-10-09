from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    GROUPS = 'GROUP'
    INDIVIDUAL = 'INDIVIDUAL'
    CAMPS = 'CAMPS'
    COURSE_TYPE = [
        (GROUPS, 'groups'),
        (INDIVIDUAL, 'individual'),
        (CAMPS, 'camps'),
    ]
    course_type = models.CharField(
        max_length=15,
        choices=COURSE_TYPE,
    )
    description = models.TextField(default='blank')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.course_type


class Levels(models.Model):
    SEAHORSE_BEGGINERS = 'Seahorse_Begginers'
    JELLYFISH_FLOATERS = 'Jellyfish_Floater'
    TURTLE_GLIDERS = 'Turtle_Gliders'
    DOLPHIN_DIVERS = 'Dolphins_Divers'
    SHARK_SPEEDSTERS = 'Shark_Speedster'
    PERSONALISED = 'Personalised'
    LEVEL = [
        (SEAHORSE_BEGGINERS, 'Seahorse_Begginers'),
        (JELLYFISH_FLOATERS, 'Jellyfish_Floaters'),
        (TURTLE_GLIDERS, 'turtle_Gliders'),
        (DOLPHIN_DIVERS, 'Dolphin_Divers'),
        (SHARK_SPEEDSTERS, 'Shark_Speedsters'),
        (PERSONALISED, 'Personalised')
    ]
    level = models.CharField(
        max_length=30,
        choices=LEVEL,
        default=SEAHORSE_BEGGINERS,
    )
    who_for = models.TextField(default='blank')
    skills = models.TextField(default='blank')

    def __str__(self):
        return self.level


class Course(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    level = models.ForeignKey('Levels', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='Course Name')
    description = models.TextField(default='')
    duration = models.TextField(default='Course duration')
    start_date = models.DateField(auto_now=False)
    start_time = models.TextField(default='Enter start time')
    end_date = models.DateField(auto_now=False)
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THRUSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'
    WEEKLY = 'Mon-Fri'
    DAY_OF_THE_WEEK = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THRUSDAY, 'Thrusday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
        (WEEKLY, 'Mon-Fri'),
    ]
    day_of_the_week = models.CharField(
        max_length=12,
        choices=DAY_OF_THE_WEEK,
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = CloudinaryField('image', default='placeholder')
    places = models.PositiveIntegerField(default=6)

    def __str__(self):
        return self.name
