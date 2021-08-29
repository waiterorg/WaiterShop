from rest_framework import routers
from django.urls import path, include
from .views import ItemViewSet

app_name = "api"

router = routers.SimpleRouter()

router.register('products', ItemViewSet, basename='product')


urlpatterns = [
    path('',include(router.urls)),
]