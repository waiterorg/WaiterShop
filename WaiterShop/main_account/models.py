from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class SocialMediaAccount(models.Model):
    name = models.CharField(max_length=150)
    facebook = models.URLField()
    tweeter = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.name


class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    social_media = models.OneToOneField(SocialMediaAccount,on_delete=models.SET_NULL, related_name='TeamMember', blank=True, null=True)
    image = models.ImageField(upload_to='users_image', blank=True, null=True)


