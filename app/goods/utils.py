"""The utils module contains helper functions for the goods app"""

from goods.models import Product


def q_search(query):
    """
    The q_search function is a helper function that allows the user to search for products by their id.
    If the query is an integer and has less than or equal to 5 digits, then it will return all products with that id.

    """
    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))
