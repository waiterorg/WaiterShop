from datetime import datetime
from factory import SubFactory
from factory.django import DjangoModelFactory
from factory import post_generation
from .models import Coupon, OrderItem, Item, Category, Order
from django.contrib.auth import get_user_model
user = get_user_model()

class CategoryFactory(DjangoModelFactory): 
    class Meta: 
        model = Category
    
    title = 'ss'
    slug = 'ww'
    status = True
    position = 2

class ItemFactory(DjangoModelFactory): 
    class Meta: 
        model = Item
    
    title = 'aa'
    price = 50
    discount_price = 20
    
    @post_generation
    def category(self, create, extracted):
        if not create:
            return
        if extracted:
            # A list of category
            for category in extracted:
                self.category.add(category)


class UserFactory(DjangoModelFactory): 
    class Meta: 
        model = user
    
    username = 'test'
    email = 'ho@sf.ui' 
    password = 'helloo'

class OrderItemFactory(DjangoModelFactory): 
    class Meta: 
        model = OrderItem
    
    ordered = False
    item = SubFactory(ItemFactory)
    quantity = 2
    user = SubFactory(UserFactory)

class CouponFactory(DjangoModelFactory): 
    class Meta: 
        model = Coupon
    
    code = 'vip client'
    amount = 20

class OrderFactory(DjangoModelFactory): 
    class Meta: 
        model = Order
    
    ordered = False
    ordered_date = datetime.now()
    user = SubFactory(UserFactory)
    coupon = SubFactory(CouponFactory)
    
    @post_generation
    def items(self, create, extracted):
        if not create:
            return
        if extracted:
            for items in extracted:
                self.items.add(items)

