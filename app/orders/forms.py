"""Forms"""

import re

from django import forms


class CreateOrderForm(forms.Form):
    """Form for creating a new order.

    Fields:
        first_name (CharField): User's first name
        last_name (CharField): User's last name
        phone_number (CharField): User's phone number
        requires_delivery (ChoiceField): Delivery required (True/False)
        delivery_address (CharField): Delivery address (optional)
        payment_on_get (ChoiceField): Payment on receipt (True/False)

    Methods
    -------
        clean_phone_number(self): Validates phone number format

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
            ("0", "False"),
            ("1", "True"),
        ],
    )

    def clean_phone_number(self):
        """Validates the format of the phone number."""
        data = self.cleaned_data["phone_number"]

        if not data.isdigit():
            raise forms.ValidationError(
                "Номер телефона должен содержать только цифры"
            )

        pattern = re.compile(r"^\d{10}$")
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data
