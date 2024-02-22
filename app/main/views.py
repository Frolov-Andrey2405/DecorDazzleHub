"""Views"""

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """View function for home page of site"""
    return HttpResponse("Home page")


def about(request):
    """View function for about page of site"""
    return HttpResponse("About page")
