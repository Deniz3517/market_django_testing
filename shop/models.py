from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Cart(models.Model):
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart #{self.id}"

    def total_price(self):
        return sum(cart_item.total_price() for cart_item in self.cartitem_set.all())


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} in cart #{self.cart.id} ({self.quantity})"
