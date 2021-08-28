from django.contrib import admin
from .models import ContactMessage, Company, TeamMember
# Register your models here.

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'readed'
                    ]
    list_filter = ['readed']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_image', 'company_team']

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'name_of_user', 'company', 'position']
    
    list_filter = ['position']
    
    search_fields = [
        'user__username',
        'company__name',
    ]


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
