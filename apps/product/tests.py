from django.test import TestCase

# Create your tests here.
from .models import Product

class ProductTest(TestCase):
    """
    Here we'll define the tests that we'll run against our Product model
    """
    def setUp(self):
        Product.objects.create(
            name='The cathedral and the bazaar',
            description='A great read',
            price=25.00,
        )
    
    def test_str(self):
        product = Product.objects.get(id=1)
        self.assertEqual(str(product), product.name)
            
