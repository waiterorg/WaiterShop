from django.db import models
from django.conf import settings
from main_account.models import SocialMediaAccount
# Create your models here.

POSITION_CHOICES = (
    ('CF','CO-Founder'),
    ('PE','Product Expert'),
    ('CM','Chief Marketing'),
    ('PS','Product Specialist'),
    ('PP','Product Photographer'),
    ('GM','General Manager'),

)



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


class CompanyManager(models.Manager):
    
    def active_company(self):
        active = self.filter(active = True)
        return active


class Company(models.Model):
    name = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    social_media = models.OneToOneField(SocialMediaAccount,on_delete=models.SET_NULL, blank=True, null=True)
    active = models.BooleanField(default=False)
    objects = CompanyManager()

    def __str__(self):
        return self.name


class TeamMemberManager(models.Manager):
    
    def active_member(self):
        active = self.filter(active = True)
        return active

class TeamMember(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name='TeamMembers')
    position = models.CharField(choices=POSITION_CHOICES, max_length=2)
    active = models.BooleanField(default=False)
    objects = TeamMemberManager()

    def __str__(self):
        return f"{self.user.username} from {self.company}"