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
