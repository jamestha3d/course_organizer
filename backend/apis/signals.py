#create user profile after user sign up

from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from .models import Profile
from emails.utils import email_user

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        #email user
        # Quick email user welcome. Commented out because it delays sign up. should be moved to profile creation signal/ remove wait to confirm if email was sent. 
        email_user(
            instance, {
                "title": "Welcome To CourseConnect",
                "message": f"Your account {instance.email} was successfully created. Please click on the link below to confirm Your account. If you did not initiate this request, Please ignore the email.",
                "emails": [instance.email]
            }
        )
    instance.profile.save()