"""Views"""

from django.shortcuts import render


def catalog(request):
    """
    The catalog function is the main page of the website.

    It displays all categories and their items,
    as well as a link to add new items.
    """
    return render(request, "goods/catalog.html")


def product(request):
    """
    The product function returns a rendered template of the product page.
    """
    return render(request, "goods/product.html")
