from rest_framework import routers
from django.urls import path, include
from .views import ItemViewSet, CompanyList, ContactMessageCreate

app_name = "api"

router = routers.SimpleRouter()

router.register('products', ItemViewSet, basename='product')


urlpatterns = [
    path('',include(router.urls)),
    path('about-us', CompanyList.as_view(), name = 'about_us'),
    path('contact-us', ContactMessageCreate.as_view(), name = 'contact_us')
]