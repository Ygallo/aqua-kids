# Generated by Django 3.2.21 on 2023-10-12 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_orderlineitem_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='eircode',
            new_name='postcode',
        ),
    ]
