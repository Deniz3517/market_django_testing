from django.test import TestCase
from shop.models import Product, Cart, CartItem

class CartServiceTest(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(name="Laptop", price=1500.00, quantity=10)
        self.product2 = Product.objects.create(name="Phone", price=1000.00, quantity=5)
        self.cart = Cart.objects.create()

    def test_add_product_to_cart(self):
        cart_item1 = CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        cart_item2 = CartItem.objects.create(cart=self.cart, product=self.product2, quantity=1)

        self.assertIn(cart_item1, self.cart.cartitem_set.all())
        self.assertIn(cart_item2, self.cart.cartitem_set.all())

    def test_cart_total_price(self):
        CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        CartItem.objects.create(cart=self.cart, product=self.product2, quantity=1)

        self.assertEqual(self.cart.total_price(), 4000.00)

    def test_update_product_quantity_in_cart(self):
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        cart_item.quantity = 3
        cart_item.save()
        self.assertEqual(cart_item.quantity, 3)
        self.assertEqual(cart_item.total_price(), 4500.00)

    def test_remove_product_from_cart(self):
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        cart_item.delete()

        self.assertNotIn(cart_item, self.cart.cartitem_set.all())
