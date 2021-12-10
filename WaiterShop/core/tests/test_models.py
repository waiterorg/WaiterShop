from datetime import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Category, Coupon, Item, Order, OrderItem
from ..factories import OrderItemFactory, OrderFactory
user = get_user_model()


class CategoryTest(TestCase):

    def test_str(self):
        # make category instance
        category = Category.objects.create(
            title='ss', slug='ww', status=True, position=2)

        self.assertEqual(str(category), category.title)

    def test_manager_filter_active_category(self):
        self.assertEqual(Category.objects.filter_active_category().count(),
                         Category.objects.filter(status=True).count())


class OrderItemTest(TestCase):
    @classmethod
    def setUpTestData(self):
        global order_item
        order_item = OrderItemFactory.create(ordered = False, item__title='shirt1', user__username = 'test_user')
    
    def test_str(self):
        self.assertEqual(str(order_item), '2 of shirt1')

    def test_order_item_name(self):
        actual_order_item_name = order_item.order_item_name()
        expected_order_item_name = '2 of shirt1'
        self.assertEqual(actual_order_item_name, expected_order_item_name)

    def test_total_item_price(self):
        actual_total_item_price = order_item.get_total_item_price()
        expect_total_item_price = 100
        self.assertEqual(actual_total_item_price, expect_total_item_price)

    def test_get_total_discount_item_price(self):
        actual_total_discount_price = order_item.get_total_discount_item_price()
        expect_total_discount_price = 40
        self.assertEqual(actual_total_discount_price,
                         expect_total_discount_price)

    def test_get_amount_saved(self):
        actual_amount_save = order_item.get_amount_saved()
        expected_amount_save = 60
        self.assertEqual(actual_amount_save, expected_amount_save)

    def test_get_final_price(self):
        actual_final_price = order_item.get_final_price()
        expected_final_price = 40
        self.assertEqual(actual_final_price, expected_final_price)


class OrderTest(TestCase):
    @classmethod
    def setUpTestData(self):
        global order
        item1 = OrderItemFactory.create(ordered = False, item__title='shirt1', user__username = 'test_user')
        item2 = OrderItemFactory.create(ordered = False, item__title='shirt2', user__username = 'test_user2')
        order = OrderFactory.create(ordered = False, ordered_date = datetime.now(), user__username = 'test1', coupon__code = 'code_test', items=(item1, item2))
    
    def test_str(self):
        self.assertEqual(str(order), '1-test1')

    def test_order_name(self):
        actual_order_name = order.order_name()
        expected_order_name = '1-test1'
        self.assertEqual(actual_order_name, expected_order_name)

    def test_get_total(self):
        actual_get_total = order.get_total()
        expected_get_total = 60
        self.assertEqual(actual_get_total, expected_get_total)
