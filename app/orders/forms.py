"""Forms"""

from django import forms


class CreateOrderForm(forms.Form):
    """
    Form for creating a new order.

    Attributes:
        first_name (CharField): First name of the customer.
        last_name (CharField): Last name of the customer.
        phone_number (CharField): Phone number of the customer.
        requires_delivery (ChoiceField): Flag indicating if the order requires delivery.
        delivery_address (CharField): Delivery address of the order. Optional.
        payment_on_get (ChoiceField): Payment method of the order.
    """
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField()
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField()
