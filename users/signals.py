import os

from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(pre_save, sender=Profile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is changed.
    """
    if not instance.pk:
        return False

    try:
        print(instance.image)
        old_file = Profile.objects.get(pk=instance.pk).image
    except Profile.DoesNotExist:
        return False

    try:
        if instance.image != old_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except Exception:
        return False

