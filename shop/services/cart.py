# shop/services/cart.py

from shop.models import Cart, Product


def create_cart():
    cart = Cart.objects.create()
    return cart


def add_product_to_cart(cart, product):
    cart.products.add(product)
    cart.save()


def remove_product_from_cart(cart, product):
    cart.products.remove(product)
    cart.save()


def update_product_quantity_in_cart(cart, product, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    cart_item = cart.products.filter(id=product.id).first()

    if cart_item:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        raise ValueError("Product not in cart")

    cart.save()


def get_cart_total_price(cart):
    total_price = sum(product.price * product.quantity for product in cart.products.all())
    return total_price
