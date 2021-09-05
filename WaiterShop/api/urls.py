from rest_framework import routers
from django.urls import path, include
from .views import ItemViewSet, CompanyList, ContactMessageCreate, add_to_cart, OrderSummary, remove_from_cart, remove_single_item_from_cart
app_name = "api"

router = routers.SimpleRouter()

router.register('products', ItemViewSet, basename='product')


urlpatterns = [
    path('',include(router.urls)),
    path('about-us/', CompanyList.as_view(), name = 'about_us'),
    path('contact-us/', ContactMessageCreate.as_view(), name = 'contact_us'),
    path('add-to-card/<slug:slug>', add_to_cart, name= 'add_to_card'),
    path('order-summary/', OrderSummary.as_view(), name = 'order-summary'),
    path('remove-from-cart/<slug:slug>', remove_from_cart, name = 'remove-from-cart'),
    path('remove-single-item/<slug:slug>', remove_single_item_from_cart, name = 'remove-single-item')

]