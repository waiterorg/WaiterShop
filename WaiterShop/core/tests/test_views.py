from django.test import TestCase
from core.models import Category
from core.models import Item
from core.models import LandingPageBanner
from django.urls import reverse
from company.models import Company
from ..factories import CategoryFactory, ItemFactory, CompanyFactory, LandingPageFactory

class HomeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ItemFactory.create()
        cls.company = CompanyFactory.create()
        cls.landing_page = LandingPageFactory.create()
        

    def test_home_view_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/home.html')

    def test_home_view_object_list(self):
        response = self.client.get('/')
        object_list = response.context['object_list'][0]
        self.assertIsInstance(object_list, Item)
    
    def test_home_view_company_context(self):
        response = self.client.get('/')
        dict_image_company = response.context['company'][0]
        company_image_url = dict_image_company['image']
        self.assertEqual(company_image_url, self.company.image)

    def test_home_view_landing_page_context(self):
        response = self.client.get('/')
        landing_page = response.context['landing_page'][0]
        self.assertIsInstance(landing_page, LandingPageBanner)

class ProductListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_item = 4
        for i in range(number_of_item):
            ItemFactory.create()

        CategoryFactory.create()

    def test_product_list_view_success(self):
        response = self.client.get(reverse('core:product-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product_list.html') 

    def test_product_list_object_list(self):
        response = self.client.get(reverse('core:product-list'))
        self.assertEqual(response.status_code, 200)
        object_list = response.context['object_list'][0]
        self.assertIsInstance(object_list, Item)
    
    def test_product_list_category_context(self):
        response = self.client.get(reverse('core:product-list'))
        self.assertEqual(response.status_code, 200)
        actual_category = response.context['categories'][0]
        expect_category = Category.objects.filter(pk=1).values('title', 'slug')[0]
        self.assertEqual(actual_category, expect_category)

    def test_product_list_pagination_is_correct(self):
        response = self.client.get(reverse('core:product-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['object_list']), 3)


class SearchListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_item = 4
        for item_id in range(number_of_item):
            ItemFactory.create(title = f"item {item_id}")

    def test_search_list_view_success(self):
        response = self.client.get(f"{reverse('core:search')}?q='test'")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/search_list.html') 

    def test_search_list_view_search_context(self):
        response = self.client.get(f"{reverse('core:search')}?q=test")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['search'], 'test')

    def test_search_list_view_object_list_with_item_parameter(self):
        # when we search 'item' object list should have all items -> per page, 3 item
        response = self.client.get(f"{reverse('core:search')}?q=item")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 3)

    def test_search_list_view_object_list_with_item_1_parameter(self):
        # when we search 'item 1' object list should have one item -> item 1 object
        response = self.client.get(f"{reverse('core:search')}?q=item 1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 1)

    def test_search_list_view_object_list_with_none_exist_item_parameter(self):
        response = self.client.get(f"{reverse('core:search')}?q=item 99")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 0)

    def test_product_list_pagination_is_correct(self):
        response = self.client.get(f"{reverse('core:search')}?q=item")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['object_list']), 3)