"""Admin site for goods app"""

from django.contrib import admin

from goods.models import Categories, Product


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Admin site for categories model"""

    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin site for products model"""

    prepopulated_fields = {"slug": ("name",)}
