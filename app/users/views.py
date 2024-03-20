"""Views"""

from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

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
                messages.success(request, f"{username}, You're logged into your account")
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
        "title": "DecorDazzleHub - Login",
        "form": form,
    }

    return render(request, "users/login.html", context)


def registration(request):
    """
    The registration function is responsible for handling the registration of new users.

    It takes a request object as its only parameter,
    returns an HttpResponseRedirect to the index page if successful,
    or renders the registration template with a UserRegistrationForm instance otherwise.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, You have successfully registered and logged into your account")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    """
    The profile function is used to update the user's profile information.

    The function first checks if the request method is POST, and if it is,
    then it creates a ProfileForm instance with data from the request.POST 
    dictionary and files from the request.FILES dictionary (the latter of which 
    will be empty in this case).

    If form validation passes, then we save() 
    our form instance and redirect back to our profile page with a success message.
    """
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Home - Кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    """
    The logout function logs the user out of their account and redirects them to the index page
    """
    messages.success(request, f"{request.user.username}, You've logged out of your account")
    auth.logout(request)
    return redirect(reverse('main:index'))
