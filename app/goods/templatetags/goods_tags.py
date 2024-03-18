"""Tags for goods app"""


from django import template
from goods.models import Categories

register = template.Library()

@register.simple_tag()
def tag_categories():
    """
    Returns all the categories in the database.
    """
    return Categories.objects.all()  # pylint: disable=E1101
