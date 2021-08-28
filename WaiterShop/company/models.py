from django.db import models
from django.conf import settings
from main_account.models import SocialMediaAccount
from django.utils.html import format_html
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
        active = self.get(active = True)
        return active


class Company(models.Model):
    name = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to='companies_image' ,blank=True, null=True)
    social_media = models.OneToOneField(SocialMediaAccount,on_delete=models.SET_NULL, blank=True, null=True)
    active = models.BooleanField(default=False)
    objects = CompanyManager()

    def __str__(self):
        return self.name

    def company_image(self):
        return format_html("<img src='{}' width=95 height=75 style='border-radius: 5px;'>".format(self.image.url))
    company_image.short_description = 'company image'

    def company_team(self):
        return ", ".join([team_member.user.username for team_member in self.TeamMembers.active_member()])
    company_team.short_description='members'


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

    def name_of_user(self):
        return self.user.username
    name_of_user.short_description = 'name'