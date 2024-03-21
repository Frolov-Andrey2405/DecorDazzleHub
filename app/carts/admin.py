"""Admin site for carts app"""

from django.contrib import admin

from carts.models import Cart

class CartTabAdmin(admin.TabularInline):
    """
    Inline admin for `Cart` model.

    `Cart` represents a user's shopping cart items.

    Attributes:
        model (class): `Cart` model.
        fields (tuple): Fields to display in the inline admin.
        search_fields (tuple): Fields to search in.
        readonly_fields (tuple): Fields to display as read-only.
        extra (int): Additional inline forms to add.
    """
    model = Cart
    fields = ("product", "quantity", "created_timestamp")
    search_fields = ("product", "quantity", "created_timestamp")
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Admin site for `Cart` model.

    Attributes:
        list_display (tuple): Fields to display in the change list.
        list_filter (tuple): Fields to filter by in the change list.
    """
    list_display = ["user_display", "product_display", "quantity", "created_timestamp"]
    list_filter = ["created_timestamp", "user", "product__name"]

    def user_display(self, obj):
        """
        Get the display name for the user
        """
        if obj.user:
            return str(obj.user)
        return "Anonymous user"

    def product_display(self, obj):
        """
        Get the display name for the product
        """
        return str(obj.product.name)
