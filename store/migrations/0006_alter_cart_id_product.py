# Generated by Django 5.0.1 on 2024-01-11 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_cart_customer_image_category_order_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="id_product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="store.product"
            ),
        ),
    ]