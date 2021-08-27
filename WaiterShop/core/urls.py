from django.urls import path
from .views import (HomeView, ItemDetailView, OrderSummaryView, 
                    add_to_cart, remove_from_cart, remove_single_item_from_cart,
                     CheckoutView, AddCouponView, PaymentView, RequestRefundView, ProductListView, CategoryList)

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


]
