# Generated by Django 4.2.7 on 2024-01-24 20:46

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0020_alter_category_image_alter_image_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="brand",
        ),
        migrations.AlterField(
            model_name="category",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                force_format="JPEG",
                keep_meta=True,
                quality=75,
                scale=0.5,
                size=[100, 100],
                upload_to="static/images",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                default=None,
                force_format="JPEG",
                keep_meta=True,
                quality=75,
                scale=0.5,
                size=[500, 500],
                upload_to="static/images/",
            ),
        ),
    ]
