from django.test import TestCase
from model_mommy import mommy
from products.models import Product


class TestProduct(TestCase):
    def setUp(self):
        self.product = mommy.make(Product, name='Apple', price=1.99)

    def test_product_creation(self):
        self.assertTrue(isinstance(self.product, Product))
