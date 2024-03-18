"""The utils module contains helper functions for the goods app"""

from django.db.models import Q
from goods.models import Product


def q_search(query):
    """
    The q_search function takes a query string and returns a queryset of products.
    """
    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))

    keywords = [
        word for word in query.split() if len(word) > 2
    ]

    q_object = Q()

    for token in keywords:
        q_object |= Q(description__icontains=token)
        q_object |= Q(name__icontains=token)

    return Product.objects.filter(q_object)
