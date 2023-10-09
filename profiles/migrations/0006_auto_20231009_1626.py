# Generated by Django 3.2.21 on 2023-10-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_rename_dob_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='Please add student name', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='special_requirements',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(default='Add student surname', max_length=50),
        ),
    ]