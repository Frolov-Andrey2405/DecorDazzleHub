"""Tags for carts app"""

from carts.models import Cart
from django import template

register = template.Library()


@register.simple_tag()
def user_carts(request):
    """
    The user_carts function returns a queryset of all the carts that belong to the user.
    If no user is logged in, it returns an empty queryset.
    """
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
