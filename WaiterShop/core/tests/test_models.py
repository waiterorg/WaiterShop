from datetime import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Category, Coupon, Item, Order, OrderItem
user = get_user_model()

class OrderItemTest(TestCase):
    @classmethod
    def setUpTestData(self):
        user_test = user.objects.create_user(username='test',email='ho@sf.ui', password='helloo')
        category = Category.objects.create(title='ss', slug='ww', status=True, position='2')
        item = Item.objects.create(title='aa',price=50, discount_price=20)
        item.category.add(category)
        self.order_item = OrderItem.objects.create(user=user_test,ordered=False,item=item,quantity=2)

    def test_order_item_name(self):
        actual_order_item_name = self.order_item.order_item_name()
        expected_order_item_name = '2 of aa'
        self.assertEqual(actual_order_item_name, expected_order_item_name)

    def test_total_item_price(self):
        actual_total_item_price = self.order_item.get_total_item_price()
        expect_total_item_price = 100
        self.assertEqual(actual_total_item_price, expect_total_item_price)

    def test_get_total_discount_item_price(self):
        actual_total_discount_price = self.order_item.get_total_discount_item_price()
        expect_total_discount_price = 40
        self.assertEqual(actual_total_discount_price, expect_total_discount_price)

    def test_get_amount_saved(self):
        actual_amount_save = self.order_item.get_amount_saved()
        expected_amount_save = 60
        self.assertEqual(actual_amount_save, expected_amount_save)
    
    def test_get_final_price(self):
        actual_final_price = self.order_item.get_final_price()
        expected_final_price = 40
        self.assertEqual(actual_final_price, expected_final_price)

class OrderTest(TestCase):
    def setUp(self):
        # create one order instance for testing

        user_test = user.objects.create_user(username='test',email='hoi@sf.ui', password='helloo')
        category = Category.objects.create(title='ss', slug='ww', status=True, position=2)
        item = Item.objects.create(title='aa',price=50, discount_price=20)
        item.category.add(category)
        coupon = Coupon.objects.create(code = 'vip client', amount = 20)
        order_item = OrderItem.objects.create(user=user_test,ordered=False,item=item,quantity=2)
        
        # for better performance used the same item witch is used in order_item -> same item in order_item & order_item2
        order_item2 = OrderItem.objects.create(user=user_test,ordered=False,item=item,quantity=3)
        
        self.order = Order.objects.create(user=user_test,ordered=False, coupon=coupon, ordered_date=datetime.now())
        self.order.items.add(order_item, order_item2)

   
    def test_order_name(self):
       actual_order_name = self.order.order_name()
       expected_order_name = '1-test'
       self.assertEqual(actual_order_name,expected_order_name)

    def test_get_total(self):
        actual_get_total = self.order.get_total()
        expected_get_total = 80
        self.assertEqual(actual_get_total,expected_get_total)