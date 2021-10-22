from django.db import models
# from django.db.models.fields.files import ImageField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profilepicture = ImageField( upload_to = 'profiles')


    def __str__(self):
        return self.user.username

@receiver (post_save, sender = User)
def create_user_profile (sender , instance , created , **kwargs):
    """Create a new profile() object when a Django user is created"""
    if created:
        Profile.objects.create(user = instance)

