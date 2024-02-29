"""Views"""

from django.shortcuts import render
from goods.models import Categories


def index(request):
    """View function for home page of site"""
    categories = Categories.objects.all()
    context = {
        "title": "DecorDazzleHub - Main",
        "content": "Furniture store 'DecorDazzleHub'",
        "categories": categories,
    }

    return render(request, "main/index.html", context)


def about(request):
    """View function for about page of site"""
    context = {
        "title": "DecorDazzleHub - About us",
        "content": "About us",
        "text_on_page": "Lorem ipsum dolor sit amet",
    }

    return render(request, "main/about.html", context)
