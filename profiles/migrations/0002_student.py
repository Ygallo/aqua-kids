# Generated by Django 3.2.21 on 2023-09-23 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_alter_course_day_of_the_week'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='blank', max_length=50)),
                ('surname', models.CharField(default='blank', max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('NON_BINARY', 'Non Binary'), ('PREFER_NOT_TO_RESPOND', 'Prefer not to respond')], max_length=25)),
                ('special_requirements', models.TextField(default='blank', max_length=200)),
                ('guardian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.levels')),
            ],
        ),
    ]
