"""Views"""

from django.contrib import auth, messages
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from carts.models import Cart
from orders.models import Order, OrderItem

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    """
    The login function is used to authenticate a user and log them into their account.
    """
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            session_key = request.session.session_key
            if user:
                auth.login(request, user)
                messages.success(
                    request, f"{username}, You're logged into your account")
                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
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
            session_key = request.session.session_key
            user = form.instance
            auth.login(request, user)
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            messages.success(
                request, f"{
                    user.username}, You have successfully registered and logged into your account")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Registration',
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

    If form validation passes, then we save() our form instance,
    redirect back to our profile page with a success message.
    """
    if request.method == 'POST':
        form = ProfileForm(
            data=request.POST,
            instance=request.user,
            files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile successfully updated")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    orders = Order.objects.filter(user=request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            ).order_by("-id")

    context = {
        'title': 'Home - Profile',
        'form': form,
        'orders': orders,
    }
    return render(request, 'users/profile.html', context)


def users_cart(request):
    """
    The users_cart function renders the users_cart.html template.
    """
    return render(request, 'users/users_cart.html')


@login_required
def logout(request):
    """
    The logout function logs the user out of their account and redirects them to the index page
    """
    messages.success(
        request, f"{
            request.user.username}, You've logged out of your account")
    auth.logout(request)
    return redirect(reverse('main:index'))
