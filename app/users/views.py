"""Views"""

from django.shortcuts import render

def login(request):
    """View function for login page of site"""
    context = {
        "title": "DecorDazzleHub - Login",
    }

    return render(request, "users/login.html", context)


def registration(request):
    """View function for registration page of site"""
    context = {
        "title": "DecorDazzleHub - Registration",
    }

    return render(request, "users/registration.html", context)


def profile(request):
    """View function for profile page of site"""
    context = {
        "title": "DecorDazzleHub - Profile",
    }

    return render(request, "users/profile.html", context)


def logout(request):
    """View function for logout page of site"""
    ...
