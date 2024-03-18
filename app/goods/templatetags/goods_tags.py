"""Tags for goods app"""

from django import template
from django.utils.http import urlencode

from goods.models import Categories

register = template.Library()


@register.simple_tag()
def tag_categories():
    """
    Returns all the categories in the database.
    """
    return Categories.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    """
    The change_params function takes a context and any number of keyword arguments.
    It returns a query string that is the result of updating the current request's GET parameters with those passed in as kwargs.
    """
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)
