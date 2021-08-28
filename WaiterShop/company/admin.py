from django.contrib import admin
from .models import ContactMessage
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'readed'
                    ]
    list_filter = ['readed']



admin.site.register(ContactMessage, ContactUsAdmin)