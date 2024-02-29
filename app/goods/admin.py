"""Admin site for goods app"""

from django.contrib import admin
from goods.models import Categories, Product

admin.site.register(Categories)
admin.site.register(Product)
