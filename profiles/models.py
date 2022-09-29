from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Model for user profiles which will maintain order history and address
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(null=True, blank=True, max_length=120)
    default_email = models.EmailField(null=True, blank=True, max_length=320)
    default_street_1 = models.CharField(null=True, blank=True, max_length=150)
    default_street_2 = models.CharField(null=True, blank=True, max_length=150)
    default_county = models.CharField(null=True, blank=True, max_length=80)
    default_postcode = models.CharField(null=True, blank=True, max_length=15)

    def __str__(self):
        """
        String method to return the username
        """
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Reciever for creating a profile if the user new, and updating when not.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
