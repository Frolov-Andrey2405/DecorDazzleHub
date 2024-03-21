"""Views"""

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from carts.models import Cart

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem

@login_required
def create_order(request):
    """
    The create_order function is responsible for creating an order.
    It takes a request as input and returns a rendered template with the form to create an order.

    If the request method is POST,
    it creates an Order object using data from the CreateOrderForm form, 
    creates OrderItem objects for each item in user's cart and clears user's cart after that. 
    """
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Create an order
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        # Create ordered items
                        for cart_item in cart_items:
                            product=cart_item.product
                            name=cart_item.product.name
                            price=cart_item.product.sell_price()
                            quantity=cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f"Insufficient quantity of product {name} in inventory. In stock - {product.quantity}")

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        # Clear user's cart after creating an order
                        cart_items.delete()

                        messages.success(request, 'Order placed!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Home - Order placement',
        'form': form,
        'orders': True,
    }
    return render(request, 'orders/create_order.html', context=context)
