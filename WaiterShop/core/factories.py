import random
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from datetime import datetime
from factory import SubFactory, post_generation, Faker, LazyAttribute, lazy_attribute
from factory.django import DjangoModelFactory
from .models import Coupon, OrderItem, Item, Category, Order


user = get_user_model()

class CategoryFactory(DjangoModelFactory): 
    class Meta: 
        model = Category
    
    title = Faker('word')
    status = True
    position = LazyAttribute(lambda x:random.randrange(1,10))
    @lazy_attribute
    def slug(self):
        return slugify(self.title)

class ItemFactory(DjangoModelFactory): 
    class Meta: 
        model = Item
    
    title = Faker('word')
    price = LazyAttribute(lambda x:random.randrange(50,100))

    discount_price = LazyAttribute(lambda x:random.randrange(10,40))
    
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
    
    username = Faker('first_name')
    email = Faker('email')
    password = Faker('word')

class OrderItemFactory(DjangoModelFactory): 
    class Meta: 
        model = OrderItem
    
    ordered = False
    item = SubFactory(ItemFactory)
    quantity = LazyAttribute(lambda x:random.randrange(1,5))
    user = SubFactory(UserFactory)

class CouponFactory(DjangoModelFactory): 
    class Meta: 
        model = Coupon
    
    code = Faker('word')
    amount = LazyAttribute(lambda x:random.randrange(5,10))

class OrderFactory(DjangoModelFactory): 
    class Meta: 
        model = Order
    
    ordered = False
    ordered_date = Faker('date_time')
    user = SubFactory(UserFactory)
    coupon = SubFactory(CouponFactory)
    
    @post_generation
    def items(self, create, extracted):
        if not create:
            return
        if extracted:
            for items in extracted:
                self.items.add(items)

