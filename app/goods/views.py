"""Views"""

import json
import os

from django.shortcuts import render


def catalog(request):
    """
    The catalog function is the main page of the website.
    """

    # Constructing the file path safely
    file_path = os.path.join(os.getcwd(), "app", "goods", "goods_list.json")

    # Reading data from goods_list.json
    with open(file_path, "r", encoding="utf-8") as json_file:
        goods_data = json.load(json_file)

    context = {
        "title": "DecorDazzleHub - Catalog",
        "goods": goods_data,
    }

    return render(request, "goods/catalog.html", context)


def product(request):
    """
    The product function returns a rendered template of the product page.
    """
    return render(request, "goods/product.html")
