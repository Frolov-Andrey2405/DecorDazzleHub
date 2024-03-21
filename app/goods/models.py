"""Models"""

from django.db import models
from django.urls import reverse


class Categories(models.Model):
    """Model for categories"""

    class Meta:
        """A class to define metadata for the Category model"""

        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=150, unique=True, verbose_name="Name")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    def __str__(self):
        """Returns a string representation of the category"""
        return f"{self.name}"


class Product(models.Model):
    """Model for products"""

    class Meta:
        """A class to define metadata for the Product model"""

        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("id",)

    name = models.CharField(max_length=150, unique=True, verbose_name="Name")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Description")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Image"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Price"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Discount"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Category"
    )

    def __str__(self):
        """Returns a string representation of the product"""
        return f"{self.name} | Quantity - {self.quantity}"

    def get_absolute_url(self):
        """
        The get_absolute_url function is used to return the URL of a product.
        This function is called by Django when it needs to get the URL for an object.
        For example, in templates you can use this syntax: {{ object.get_absolute_url }}
        """
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        """Returns a string representation of the product ID"""
        return f"{self.id:05}"

    def sell_price(self):
        """
        Returns the price of a product after applying any discount.
        If no discount is applied, it simply returns the original price.
        """
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
