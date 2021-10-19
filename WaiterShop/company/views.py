from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib import messages
from .models import ContactMessage, Company
from .forms import ContactForm
# Create your views here.

class ContactUsView(View):
    def get(self, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(self.request, "shop/contact-us.html", context)
    
    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                ContactMassage = ContactMessage()
                ContactMassage.name = name
                ContactMassage.email = email
                ContactMassage.subject = subject
                ContactMassage.massage = message
                ContactMassage.save()
                messages.success(self.request,"Your message has been successfully sent.")
                return redirect("core:home")
            except:
                messages.warning(self.request,"something is wrong !")
                return redirect("core:contact-us")

class AboutUsView(View):
    def get(self, *args, **kwargs):
        company = Company.objects.filter_active_company().select_related('social_media').first()
        team_member = company.TeamMembers.active_member().select_related('user','user__social_media')

        context = {
            'company': company,
            'team_member': team_member
        }
        return render(self.request, 'shop/about-us.html', context)
