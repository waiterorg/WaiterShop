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

    def test_product_list_pagination_returns_404_page_out_of_range(self):
        response = self.client.get(reverse('core:product-list', kwargs={'page': 999}))
        self.assertEqual(response.status_code, 404)
