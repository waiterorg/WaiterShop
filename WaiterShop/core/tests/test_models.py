from datetime import datetime
from django.test import TestCase
from ..models import Category
from ..factories import CategoryFactory, OrderItemFactory, OrderFactory



class CategoryTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = CategoryFactory.create(title = 'cloths i am windo64%$^')
 
    def test_str(self):
        """Category instance string"""
        self.assertEqual(str(self.category), self.category.title)

    def test_manager_filter_active_category(self):
        """Filter active category manager for category instances with true status"""
        self.assertEqual(Category.objects.filter_active_category().count(),
                         Category.objects.filter(status=True).count())


class OrderItemTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = CategoryFactory.create()
        cls.order_item = OrderItemFactory.create(item__category =(category,), item__image = None)
    

    def test_str(self):
        """Order item instance string"""
        self.assertEqual(str(self.order_item), f"{self.order_item.quantity} of {self.order_item.item.title}")

    def test_order_item_name(self):
        """Order item name method which is quantity of title"""
        actual_order_item_name = self.order_item.order_item_name()
        expected_order_item_name = f"{self.order_item.quantity} of {self.order_item.item.title}"
        self.assertEqual(actual_order_item_name, expected_order_item_name)

    def test_total_item_price(self):
        """Total price for order item which is quantity multiple item price"""
        actual_total_item_price = self.order_item.get_total_item_price()
        expect_total_item_price = self.order_item.quantity * self.order_item.item.price
        self.assertEqual(actual_total_item_price, expect_total_item_price)

    def test_get_total_discount_item_price(self):
        """Total discount for order item which is quantity multiple item discount price"""
        actual_total_discount_price = self.order_item.get_total_discount_item_price()
        expect_total_discount_price = self.order_item.quantity * self.order_item.item.discount_price
        self.assertEqual(actual_total_discount_price,
                         expect_total_discount_price)

    def test_get_amount_saved(self):
        """Amount saved is the difference between ordinary price and discount price"""
        actual_amount_save = self.order_item.get_amount_saved()
        expected_amount_save = self.order_item.get_total_item_price() - self.order_item.get_total_discount_item_price()
        self.assertEqual(actual_amount_save, expected_amount_save)

    def test_get_final_price(self):
        """
        If item has dicount price used total discount price method
        but if item has not disount price used total item price method
        for calculation
        """
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
    
    def test_str(self):
        """Order instance string"""
        self.assertEqual(str(self.order), f"{self.order.pk}-{self.order.user.username}")

    def test_order_name(self):
        """Order name method which is primary key - username"""
        actual_order_name = self.order.order_name()
        expected_order_name = f"{self.order.pk}-{self.order.user.username}"
        self.assertEqual(actual_order_name, expected_order_name)

    def test_get_total(self):
        """
        Final price which is sum of order items , if order had coupon
        final price equals to final price minus coupon   
        """
        actual_get_total = self.order.get_total()
        expected_get_total = 0
        for order_item in self.order.items.all():
            expected_get_total += order_item.get_final_price()
        if self.order.coupon:
            expected_get_total -= self.order.coupon.amount
        self.assertEqual(actual_get_total, expected_get_total)
