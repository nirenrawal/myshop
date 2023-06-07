from django.test import TestCase
from .models import Address, Brand, Category, Product, Feedback

class ModelTests(TestCase):
    def test_address_model(self):
        address = Address.objects.create(street="Sample Street", zipcode=12345, city="Sample City", country="Sample Country")
        self.assertEqual(str(address), "Sample Country - Sample City")

    def test_brand_model(self):
        address = Address.objects.create(street="Sample Street", zipcode=12345, city="Sample City", country="Sample Country")
        brand = Brand.objects.create(title="Sample Brand", logo="path/to/logo.jpg", address=address)
        self.assertEqual(str(brand), "Sample Brand")

    def test_category_model(self):
        category = Category.objects.create(title="Sample Category", description="Sample description")
        self.assertEqual(str(category), "Sample Category")

   
    
