"""Views"""

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm

def login(request):
    """
    The login function is a view that allows users to login.
    It takes in the request and returns a rendered template of the login page.
    If the user submits valid credentials,
    they are authenticated and redirected to their profile page.
    """
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
        "title": "DecorDazzleHub - Login",
        "form": form,
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
