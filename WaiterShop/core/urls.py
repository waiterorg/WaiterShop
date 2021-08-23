from django.urls import path
from .views import HomeView, ItemDetailView, OrderSummaryView, add_to_cart

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug:slug>', ItemDetailView.as_view(), name='item_detail'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
]