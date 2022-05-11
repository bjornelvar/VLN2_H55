from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profiles
import os


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profiles.objects.create(user=instance)

@receiver(pre_save, sender=Profiles)
def delete_old_profile_pic(sender, instance, **kwargs):
    print("Signal received")
    if instance._state.adding and not instance.pk:
        return False

    try:
        old_photo = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    if instance.image and old_photo.name != 'images/blank-profile-picture.png':
            photo = instance.image
            if not old_photo == photo:
                if os.path.isfile(old_photo.path):
                    os.remove(old_photo.path)