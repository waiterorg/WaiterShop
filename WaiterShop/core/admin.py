from django.contrib import admin
from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile, Category, LandingPageBanner

# Register your models here.
def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)

make_refund_accepted.short_description = 'Update orders to refund granted'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name',
                    'user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'payment',
                    'coupon'
                    )
    list_display_links = (
        'user',
        'shipping_address',
        'payment',
        'coupon'
    )
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    
    actions = [make_refund_accepted]

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'default'
    ]
    list_filter = ['default', 'country']
    search_fields = ['user__username', 'street_address', 'apartment_address', 'zip']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'quantity',
                    ]
    list_display_links = [
        'user',
    ]


admin.site.register(Item)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(LandingPageBanner)



