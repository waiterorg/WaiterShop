from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.urls import path
from django.views.decorators.cache import cache_page
from .views import (HomeView, ItemDetailView, OrderSummaryView, 
                    add_to_cart, remove_from_cart, remove_single_item_from_cart,
                     CheckoutView, AddCouponView, PaymentView, RequestRefundView, ProductListView,
                      CategoryList, SearchList)

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/detail/<slug:slug>', ItemDetailView.as_view(), name='item_detail'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/page/<int:page>', ProductListView.as_view(), name='product-list'),
    path('products/<slug:slug>', CategoryList.as_view(), name='product-category'),
    path('products/<slug:slug>/page/<int:page>', CategoryList.as_view(), name='product-category'),
    path('search/', SearchList.as_view(), name="search"),
    path('search/page/<int:page>', SearchList.as_view(), name="search"),


]
