# Generated by Django 5.0.2 on 2024-03-20 18:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0001_initial"),
        ("goods", "0003_alter_product_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cart",
            options={"verbose_name": "Cart", "verbose_name_plural": "Carts"},
        ),
        migrations.AlterField(
            model_name="cart",
            name="created_timestamp",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Date added"
            ),
        ),
        migrations.AlterField(
            model_name="cart",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="goods.product",
                verbose_name="Product",
            ),
        ),
        migrations.AlterField(
            model_name="cart",
            name="quantity",
            field=models.PositiveSmallIntegerField(
                default=0, verbose_name="Quantity"
            ),
        ),
        migrations.AlterField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]
