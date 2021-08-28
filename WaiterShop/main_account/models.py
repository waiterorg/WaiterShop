from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class SocialMediaAccount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, blank=True, null=True)
    facebook = models.URLField()
    tweeter = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.user.username


class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    social_media = models.OneToOneField(SocialMediaAccount,on_delete=models.SET_NULL, related_name='TeamMember', blank=True, null=True)
    image = models.ImageField(upload_to='users_image', blank=True, null=True)


