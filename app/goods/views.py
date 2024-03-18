"""Views"""

from django.shortcuts import render

from goods.models import Product

def catalog(request):
    """
    The catalog function is the main page of the website.
    """
    goods = Product.objects.all()

    context = {
        "title": "DecorDazzleHub - Catalog",
        "goods": goods,
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_id):
    """
    The product function returns a rendered template of the product page.
    """
    product_instance = Product.objects.get(id=product_id)

    context = {
        "product": product_instance,
    }

    return render(request, "goods/product.html", context=context)
