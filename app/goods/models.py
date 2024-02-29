"""Models"""

from django.db import models


class Categories(models.Model):
    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=150, unique=True, verbose_name="Name")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )


class Product(models.Model):
    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    name = models.CharField(max_length=150, unique=True, verbose_name="Name")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Description"
    )
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
