from django.contrib import admin
from .models import ContactMessage, Company, TeamMember
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'readed'
                    ]
    list_filter = ['readed']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_image', 'company_team']


admin.site.register(ContactMessage, ContactUsAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(TeamMember)
