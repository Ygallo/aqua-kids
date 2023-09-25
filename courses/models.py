from django.db import models

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
    SEAHORSE_BEGGINERS = 'SEAHORSE_BEGGINERS'
    JELLYFISH_FLOATERS = 'JELLYFISH_FLOATER'
    TURTLE_GLIDERS = 'TURTLE_GLIDERS'
    DOLPHIN_DIVERS = 'DOLPHIN_DIVERS'
    SHARK_SPEEDSTERS = 'SHARK_SPEEDSTERS'
    LEVEL = [
        (SEAHORSE_BEGGINERS, 'seahorse_begginers'),
        (JELLYFISH_FLOATERS, 'jellyfish_floaters'),
        (TURTLE_GLIDERS, 'turtle_gliders'),
        (DOLPHIN_DIVERS, 'dolphin_divers'),
        (SHARK_SPEEDSTERS, 'shark_speedsters'),
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
    name = models.CharField(max_length=250, default='blank')
    description = models.TextField(default='blank')
    duration = models.TextField(default='blank')
    start_date = models.DateField(auto_now=False)
    start_time = models.TextField(default='blank')
    end_date = models.DateField(auto_now=False)
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THRUSDAY = 'THRUSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'
    DAY_OF_THE_WEEK = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THRUSDAY, 'Thrusday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]
    day_of_the_week = models.CharField(
        max_length=12,
        choices=DAY_OF_THE_WEEK,
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    places = models.PositiveIntegerField(default=6)

    def __str__(self):
        return self.name
