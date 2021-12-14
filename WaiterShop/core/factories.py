import random
from django.contrib.auth import get_user_model
from django.template.defaultfilters import length, slugify
from django.core.files.base import ContentFile
from factory import (SubFactory, 
                    post_generation, Faker, LazyAttribute,
                    lazy_attribute, fuzzy )
from factory.django import DjangoModelFactory, ImageField

from main_account.models import SocialMediaAccount
from company.models import Company
from .models import Coupon, LandingPageBanner, OrderItem, Item, Category, Order


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
    status = True
    discount_price = LazyAttribute(lambda x:random.randrange(10,40))
    image = LazyAttribute(
            lambda _: ContentFile(
                ImageField()._make_data(
                    {'width': 1024, 'height': 768}
                ), 'example.jpg'
            )
        )
    

    @lazy_attribute
    def slug(self):
        return slugify(self.title)

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

class SocialMediaAccountFactory(DjangoModelFactory): 
    class Meta: 
        model = SocialMediaAccount
    
    name = Faker('word')
    facebook = LazyAttribute(lambda x: 'https://fa-{}.com'.format(x.name))
    tweeter = LazyAttribute(lambda x: 'https://tw-{}.com'.format(x.name))
    linkedin = LazyAttribute(lambda x: 'https://li-{}.com'.format(x.name))


class CompanyFactory(DjangoModelFactory): 
    class Meta: 
        model = Company
    
    name = Faker('company')
    title = fuzzy.FuzzyText(length=15)
    description = fuzzy.FuzzyText(length=45)
    social_media = SubFactory(SocialMediaAccountFactory)
    active = True

    image = LazyAttribute(
            lambda _: ContentFile(
                ImageField()._make_data(
                    {'width': 1024, 'height': 768}
                ), 'example.jpg'
            )
        )
    

class LandingPageFactory(DjangoModelFactory): 
    class Meta: 
        model = LandingPageBanner
    
    tag = fuzzy.FuzzyChoice(['BO','FD','LM'])
    title = fuzzy.FuzzyText(length=15)
    status = True