from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Cart(models.Model):
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Cart #{self.id}"

    def total_price(self):
        return sum(product.price for product in self.products.all())
