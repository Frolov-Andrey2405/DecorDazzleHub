"""Admin site for users app"""

from django.contrib import admin
from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin site for `User` model.

    Attributes:
        list_display (tuple): Fields to display in the change list.
        search_fields (tuple): Fields to search in the change list.
        inlines (tuple): Inline admin classes to display.
    """
    list_display = ["username", "first_name", "last_name", "email",]
    search_fields = ["username", "first_name", "last_name", "email",]
    inlines = [CartTabAdmin, OrderTabulareAdmin]
