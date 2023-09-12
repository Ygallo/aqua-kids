# Generated by Django 3.2.21 on 2023-09-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='course_type',
            field=models.CharField(choices=[('GROUP', 'groups'), ('INDIVIDUAL', 'individual'), ('CAMPS', 'camps')], max_length=15),
        ),
        migrations.AlterField(
            model_name='course',
            name='day_of_the_week',
            field=models.CharField(choices=[('MONDAY', 'monday'), ('TUESDAY', 'tuesday'), ('WEDNESDAY', 'wednesday'), ('THRUSDAY', 'thrusday'), ('FRIDAY', 'friday'), ('SATURDAY', 'saturday'), ('SUNDAY', 'sunday')], max_length=12),
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('SEAHORSE_BEGGINERS', 'seahorse_begginers'), ('JELLYFISH_FLOATER', 'jellyfish_floaters'), ('TURTLE_GLIDERS', 'turtle_gliders'), ('DOLPHIN_DIVERS', 'dolphin_divers'), ('SHARK_SPEEDSTERS', 'shark_speedsters')], default='SEAHORSE_BEGGINERS', max_length=30),
        ),
    ]
