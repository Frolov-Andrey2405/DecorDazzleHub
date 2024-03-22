"""Admin site for goods app"""

from django.contrib import admin

from goods.models import Categories, Product


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Admin site for Categories model"""

    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
    ]


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    """Admin site for Product model.

    Attributes
    ----------
        prepopulated_fields (dict): Fields to prepopulate.
        list_display (tuple): Fields to display in the change list.
        list_editable (tuple): Fields to make editable in the change list.
        search_fields (tuple): Fields to search by.
        list_filter (tuple): Fields to filter by in the change list.
        fields (tuple): Fields to display in the change form.

    """

    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = [
        "discount",
    ]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category"]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
    ]
