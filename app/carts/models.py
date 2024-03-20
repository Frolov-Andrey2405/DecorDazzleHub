"""Models"""

from django.db import models
from goods.models import Product
from users.models import User


class CartQueryset(models.QuerySet):
    """QuerySet for cart"""

    def total_price(self):
        """
        Returns the sum of all products in the cart
        """
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        """
        Returns the sum of all quantities in the cart
        """
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    """Model for cart"""
    class Meta:
        """Meta"""
        db_table = "cart"
        verbose_name = "Cart"
        verbose_name_plural = "Cart"

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="User",
    )
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, verbose_name="Product"
    )
    quantity = models.PositiveSmallIntegerField(
        default=0, verbose_name="Quantity")
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Date added"
    )

    objects = CartQueryset().as_manager()

    def products_price(self):
        """
        The products_price function returns the total price of all products in a cart.

        It does this by multiplying the sell_price of each product by its quantity,
        then adding them together.
        """
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        """
        The __str__ function is used to return a string representation of the object.

        This function is called when you use print() on an object,
        or when str() is used on an object.

        The __str__ method should return a string that can be understood by humans.
        """
        return f"Cart {
            self.user.username} | Product {
            self.product.name} | Quantity {
            self.quantity}"
