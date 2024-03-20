"""Admin site for carts app"""

from django.contrib import admin

from carts.models import Cart

admin.site.register(Cart)
