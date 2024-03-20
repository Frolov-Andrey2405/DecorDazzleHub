"""Views"""

from django.shortcuts import redirect
from goods.models import Product

from carts.models import Cart


def cart_add(request, product_slug):
    """
    The cart_add function is used to add a product to the cart.
    It takes in a request and product_slug as parameters.

    The function first gets the product from the database using its slug,
    then checks if user is authenticated or not. If user is authenticated,
    it filters all carts that have same user and same product as current one,
    then checks if any of those carts exist or not
    (if they do exist it means that this particular item has already been added to cart).

    If there are no such items in cart yet, we create one with quantity 1.
    """
    product = Product.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META["HTTP_REFERER"])


def cart_change(request, product_slug): ...


def cart_remove(request, product_slug): ...
