#create user profile after user sign up

from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()