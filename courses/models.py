from django.db import models

# Create your models here.


class Category(models.Model):
    GROUPS = 'GR'
    INDIVIDUAL = 'IN'
    CAMPS = 'CA'
    COURSE_TYPE = [
        (GROUPS, 'groups'),
        (INDIVIDUAL, 'individual'),
        (CAMPS, 'camps'),
    ]
    course_type = models.CharField(
        max_length=2,
        choices=COURSE_TYPE,
    )

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    SEAHORSE_BEGGINERS = 'SH'
    JELLYFISH_FLOATERS = 'JF'
    TURTLE_GLIDERS = 'TG'
    DOLPHIN_DIVERS = 'DD'
    SHARK_SPEEDSTERS = 'SS'
    LEVEL = [
        (SEAHORSE_BEGGINERS, 'seahorse_begginers'),
        (JELLYFISH_FLOATERS, 'jellyfish_floaters'),
        (TURTLE_GLIDERS, 'turtle_gliders'),
        (DOLPHIN_DIVERS, 'dolphin_divers'),
        (SHARK_SPEEDSTERS, 'shark_speedsters'),
    ]
    level = models.CharField(
        max_length=2,
        choices=LEVEL,
        default=SEAHORSE_BEGGINERS,
    )
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THRUSDAY = 'TH'
    FRIDAY = 'FR'
    SATURDAY = 'SA'
    SUNDAY = 'SU'
    DAY_OF_THE_WEEK = [
        (MONDAY, 'monday'),
        (TUESDAY, 'tuesday'),
        (WEDNESDAY, 'wednesday'),
        (THRUSDAY, 'thrusday'),
        (FRIDAY, 'friday'),
        (SATURDAY, 'saturday'),
        (SUNDAY, 'sunday'),
    ]
    day_of_the_week = models.CharField(
        max_length=2,
        choices=DAY_OF_THE_WEEK,
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    places = models.PositiveIntegerField(default=6)

    def __str__(self):
        return self.name
