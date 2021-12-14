from datetime import datetime
from django.test import TestCase
from unittest import skip
from ..models import Category, Order, OrderItem
from ..factories import CategoryFactory, OrderItemFactory, OrderFactory



class CategoryTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = CategoryFactory.create(title = 'cloths i am windo64%$^')
 
    def test_str(self):
        self.assertEqual(str(self.category), self.category.title)

    def test_manager_filter_active_category(self):
        self.assertEqual(Category.objects.filter_active_category().count(),
                         Category.objects.filter(status=True).count())


class OrderItemTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = CategoryFactory.create()
        cls.order_item = OrderItemFactory.create(item__category =(category,), item__image = None)
    
    def test_order_item_creation(self):
        self.assertIsInstance(self.order_item, OrderItem)

    def test_str(self):
        self.assertEqual(str(self.order_item), f"{self.order_item.quantity} of {self.order_item.item.title}")

    def test_order_item_name(self):
        actual_order_item_name = self.order_item.order_item_name()
        expected_order_item_name = f"{self.order_item.quantity} of {self.order_item.item.title}"
        self.assertEqual(actual_order_item_name, expected_order_item_name)

    def test_total_item_price(self):
        actual_total_item_price = self.order_item.get_total_item_price()
        expect_total_item_price = self.order_item.quantity * self.order_item.item.price
        self.assertEqual(actual_total_item_price, expect_total_item_price)

    def test_get_total_discount_item_price(self):
        actual_total_discount_price = self.order_item.get_total_discount_item_price()
        expect_total_discount_price = self.order_item.quantity * self.order_item.item.discount_price
        self.assertEqual(actual_total_discount_price,
                         expect_total_discount_price)

    def test_get_amount_saved(self):
        actual_amount_save = self.order_item.get_amount_saved()
        expected_amount_save = self.order_item.get_total_item_price() - self.order_item.get_total_discount_item_price()
        self.assertEqual(actual_amount_save, expected_amount_save)

    def test_get_final_price(self):
        actual_final_price = self.order_item.get_final_price()
        if self.order_item.item.discount_price:
            expected_final_price = self.order_item.get_total_discount_item_price()
        else:
            expected_final_price = self.order_item.get_total_item_price()
        self.assertEqual(actual_final_price, expected_final_price)


class OrderTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        global order
        order_item1 = OrderItemFactory.create(ordered = False, user__username = 'test_user', item__image = None)
        order_item2 = OrderItemFactory.create(ordered = False, user__username = 'test_user2', item__image = None)
        cls.order = OrderFactory.create(ordered = False, ordered_date = datetime.now(), user__username = 'test1', coupon__code = 'code_test', items=(order_item1, order_item2))
    
    def test_order_creation(self):
        self.assertIsInstance(self.order, Order)
    
    def test_str(self):
        self.assertEqual(str(self.order), f"{self.order.pk}-{self.order.user.username}")

    def test_order_name(self):
        actual_order_name = self.order.order_name()
        expected_order_name = f"{self.order.pk}-{self.order.user.username}"
        self.assertEqual(actual_order_name, expected_order_name)

    def test_get_total(self):
        actual_get_total = self.order.get_total()
        expected_get_total = 0
        for order_item in self.order.items.all():
            expected_get_total += order_item.get_final_price()
        if self.order.coupon:
            expected_get_total -= self.order.coupon.amount
        self.assertEqual(actual_get_total, expected_get_total)
