"""Views"""

from django.http import JsonResponse
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


def cart_change(request):
    """
    The cart_change function is called when the user changes
    the quantity of a product in their cart.

    The function takes two parameters: request and cart_id.

    The request parameter is used to get information from the POST method,
    which contains information about what item was changed and how much it was changed by.

    The cart_id parameter is used to identify which item in
    the database needs to be updated with new data.
    """
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")
    cart = Cart.objects.get(id=cart_id)
    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity
    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "includes/included_cart.html", {"carts": cart}, request=request)
    response_data = {
        "message": "Quantity changed",
        "cart_items_html": cart_items_html,
        "quaantity": updated_quantity,
    }
    return JsonResponse(response_data)


def cart_remove(request):
    """
    The cart_remove function is called when the user clicks on the 'Remove' button in their cart.

    The function deletes the item from their cart and returns a JsonResponse with a message, 
    the updated HTML for their cart, and how many items were deleted.
    """
    cart_id = request.POST.get("cart_id")
    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "includes/included_cart.html", {"carts": user_cart}, request=request)
    response_data = {
        "message": "Product deleted",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }
    return JsonResponse(response_data)
