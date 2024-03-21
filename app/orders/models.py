"""Models"""

from django.db import models

from goods.models import Product
from users.models import User


class OrderItemQuerySet(models.QuerySet):
    """
    QuerySet for order items.

    Methods:
        total_price(self) - Returns the sum of all products in the order.
        total_quantity(self) - Returns the sum of all quantities in the order.
    """

    def total_price(self):
        """
        Returns the sum of all products in the order.
        """
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        """
        Returns the sum of all quantities in the order.
        """
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    """
    Model for user orders.

    Fields:
        user - foreign key to User model, on delete - set default, blank=True, null=True, verbose_name="User", default=None
        created_timestamp - date time field, auto_now_add=True, verbose_name="Date of order creation"
        phone_number - char field, max_length=20, verbose_name="Phone number"
        requires_delivery - boolean field, default=False, verbose_name="Delivery required"
        delivery_address - text field, null=True, blank=True, verbose_name="Delivery address"
        payment_on_get - boolean field, default=False, verbose_name="Payment on receipt"
        is_paid - boolean field, default=False, verbose_name="Paid"
        status - char field, max_length=50, default='In processing', verbose_name="Order status"

    Methods:
        __str__(self) - returns string representation of the order, including order number and buyer's name
    """

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_DEFAULT,
        blank=True,
        null=True,
        verbose_name="User",
        default=None,
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Date of order creation"
    )
    phone_number = models.CharField(max_length=20, verbose_name="Phone number")
    requires_delivery = models.BooleanField(
        default=False, verbose_name="Delivery required"
    )
    delivery_address = models.TextField(
        null=True, blank=True, verbose_name="Delivery address"
    )
    payment_on_get = models.BooleanField(
        default=False, verbose_name="Payment on receipt"
    )
    is_paid = models.BooleanField(default=False, verbose_name="Paid")
    status = models.CharField(
        max_length=50, default="In processing", verbose_name="Order status"
    )

    class Meta:
        """Meta"""

        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        """
        Returns string representation of the order, including order number and buyer's name.
        """
        return (
            f"Order  № {
                self.pk} | Buyer  {
                self.user.first_name} {
                self.user.last_name}")


class OrderItem(models.Model):
    """
    Model representing a product sold in an order.
    Fields:
        order - foreign key to Order model, on delete - cascade, verbose_name="Order"
        product - foreign key to Product model, on delete - set default, null=True, verbose_name="Product", default=None
        name - char field, max_length=150, verbose_name="Title"
        price - decimal field, max_digits=7, decimal_places=2, verbose_name="Price"
        quantity - positive integer field, default=0, verbose_name="Quantity"
        created_timestamp - date time field, auto_now_add=True, verbose_name="Date of Sale"

    Methods:
        products_price(self) - returns the total price of the sold product
    """

    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        verbose_name="Order")
    product = models.ForeignKey(
        to=Product,
        on_delete=models.SET_DEFAULT,
        null=True,
        verbose_name="Product",
        default=None,
    )
    name = models.CharField(max_length=150, verbose_name="Title")
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name="Price")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Date of Sale"
    )

    class Meta:
        """Meta"""

        db_table = "order_item"
        verbose_name = "Sold product"
        verbose_name_plural = "Goods sold"

    objects = OrderItemQuerySet.as_manager()

    def products_price(self):
        """
        Returns the total price of the sold product.
        """
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        """
        Returns string representation of the sold product, including product name and order number.
        """
        return f"Item {self.name} | Order № {self.order.pk}"
