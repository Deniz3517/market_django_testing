# shop/services.py
from .models import Product, Cart


def create_cart():
    return Cart.objects.create()


def add_product_to_cart(cart, product):
    cart.products.add(product)
    cart.save()


def remove_product_from_cart(cart, product):
    cart.products.remove(product)
    cart.save()
