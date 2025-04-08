# shop/tests/test_services.py
from django.test import TestCase
from shop.models import Product, Cart
from shop.services import create_cart, add_product_to_cart, remove_product_from_cart


class CartServiceTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Laptop", price=1500.00)
        self.cart = create_cart()

    def test_create_cart(self):
        self.assertIsInstance(self.cart, Cart)

    def test_add_product_to_cart(self):
        add_product_to_cart(self.cart, self.product)
        self.assertIn(self.product, self.cart.products.all())

    def test_remove_product_from_cart(self):
        add_product_to_cart(self.cart, self.product)
        remove_product_from_cart(self.cart, self.product)
        self.assertNotIn(self.product, self.cart.products.all())

    def test_cart_total_price(self):
        product2 = Product.objects.create(name="Phone", price=1000.00)
        add_product_to_cart(self.cart, self.product)
        add_product_to_cart(self.cart, product2)
        self.assertEqual(self.cart.total_price(), 2500.00)
