from django.test import TestCase
from core.models import Item
from core.models import LandingPageBanner

from company.models import Company
from ..factories import ItemFactory, CompanyFactory, LandingPageFactory

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


       