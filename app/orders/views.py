"""Views"""

from django.shortcuts import render


def create_order(request):
    """
    The create_order function is responsible for creating a new order.
        It takes in the request object and returns an HTML page with a form to create an order.
    """
    return render(request, 'orders/create_order.html')
