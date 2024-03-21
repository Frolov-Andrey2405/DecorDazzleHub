"""Utils"""

from carts.models import Cart


def get_user_carts(request):
    """
    The get_user_carts function returns a list of all the carts that belong to the user.
        If no user is logged in, it returns an empty list.
    """
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
