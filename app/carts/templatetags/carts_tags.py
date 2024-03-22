"""Tags for carts app"""

from django import template

from carts.utils import get_user_carts

register = template.Library()


@register.simple_tag()
def user_carts(request):
    """Returns a list of all the carts that belong to the user.
    The function takes in a request object and returns a list of cart objects.
    """
    return get_user_carts(request)
