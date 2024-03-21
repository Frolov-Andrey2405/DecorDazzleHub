"""Utils"""

from carts.models import Cart


def get_user_carts(request):
    """
    The get_user_carts function returns a queryset of all the carts that belong to the user.

    If the user is not authenticated,
    it will return all carts that have been created with this session key.
    """
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key)
