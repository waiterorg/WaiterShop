from django.db import models
from django.conf import settings
# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length = 150)
    subject = models.CharField(max_length = 150)
    massage = models.TextField()
    email = models.EmailField()
    readed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Client message'
        verbose_name_plural = 'Client messages'


    def __str__(self):
        return f"{self.subject} from {self.name}"

