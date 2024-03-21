"""Forms"""

from django import forms


class CreateOrderForm(forms.Form):
    """
    Form for creating a new order.

    Fields:
        first_name (CharField): First name of the client
        last_name (CharField): Last name of the client
        phone_number (CharField): Phone number of the client
        requires_delivery (ChoiceField): Does the order require delivery (boolean)
        delivery_address (CharField): Address for delivery (optional)
        payment_on_get (ChoiceField): Is the order paid on delivery (boolean)
    """

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
            ],
        )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
            ],
        )
