from django.test import TestCase
from shop.models import Product, Cart, CartItem

class CartServiceTest(TestCase):

    def setUp(self):
        # Ürünleri ve sepete eklemek için gerekli verileri oluşturuyoruz
        self.product1 = Product.objects.create(name="Laptop", price=1500.00, quantity=10)
        self.product2 = Product.objects.create(name="Phone", price=1000.00, quantity=5)
        self.cart = Cart.objects.create()

    def test_add_product_to_cart(self):
        # Sepete ürün ekliyoruz
        cart_item1 = CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        cart_item2 = CartItem.objects.create(cart=self.cart, product=self.product2, quantity=1)

        # Sepet içinde ürünlerin olduğunu doğruluyoruz
        self.assertIn(cart_item1, self.cart.cartitem_set.all())
        self.assertIn(cart_item2, self.cart.cartitem_set.all())

    def test_cart_total_price(self):
        # Sepete ürün ekliyoruz
        CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        CartItem.objects.create(cart=self.cart, product=self.product2, quantity=1)

        # Sepetin toplam fiyatını kontrol ediyoruz
        self.assertEqual(self.cart.total_price(), 4000.00)

    def test_update_product_quantity_in_cart(self):
        # Ürün miktarını güncelleme
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)

        # Ürün miktarını değiştiriyoruz
        cart_item.quantity = 3
        cart_item.save()

        # Güncellenen miktarın doğru olduğunu kontrol ediyoruz
        self.assertEqual(cart_item.quantity, 3)
        self.assertEqual(cart_item.total_price(), 4500.00)  # Yeni fiyat 1500 * 3 = 4500

    def test_remove_product_from_cart(self):
        # Sepetten ürün çıkarma
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        cart_item.delete()

        # Sepette ürün olup olmadığını kontrol ediyoruz
        self.assertNotIn(cart_item, self.cart.cartitem_set.all())
