"""Views"""

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """View function for home page of site"""
    context = {
        "title": "DecorDazzleHub",
        "content": "Page content",
        "list": ["first", "second"],
        "dict": {"first": 1},
        "is_authenticated": True,
    }

    return render(request, 'main/index.html', context)


def about(request):
    """View function for about page of site"""
    return HttpResponse("About page")
