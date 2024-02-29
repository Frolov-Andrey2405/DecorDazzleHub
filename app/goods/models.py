"""Models"""

from django.db import models


class Categories(models.Model):
    class Meta:
        db_table = "categories"

    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
