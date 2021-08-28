from django.urls import path
from .views import ContactUsView


app_name = 'company'
urlpatterns = [
    path('contact-us', ContactUsView.as_view(),name = 'contact-us'),
]