# Generated by Django 4.2.7 on 2024-01-29 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0023_order_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cart",
            old_name="id_product",
            new_name="product",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="address",
        ),
        migrations.AddField(
            model_name="customer",
            name="user",
            field=models.OneToOneField(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="store.product"
            ),
        ),
    ]