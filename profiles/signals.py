from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import User, Student


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


@receiver(post_save, sender=User)
def create_or_update_student(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Student.objects.create(user=instance)
    # Existing users: just save the profile
    instance.student.save()
