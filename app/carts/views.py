"""Views"""

from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from carts.models import Cart
from carts.utils import get_user_carts  # pylint: disable=E0401, E0611

from goods.models import Product


def cart_add(request):
    """
    The cart_add function is called when a user clicks the 'Add to Cart' button on a product page
    """
    product_id = request.POST.get("product_id")
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "includes/included_cart.html", {"carts": user_cart}, request=request)
    response_data = {
        "message": "Product has been added to your cart",
        "cart_items_html": cart_items_html,
    }
    return JsonResponse(response_data)


def cart_change(request, product_slug):
    ...


def cart_remove(request, cart_id):
    """
    The cart_remove function removes a product from the cart.
    It takes in a request and an id of the cart to be removed, then deletes it.
    Finally, it redirects back to where you came from.
    """
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
