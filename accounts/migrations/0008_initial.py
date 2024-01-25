# Generated by Django 4.2.7 on 2024-01-25 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0007_delete_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Muž"), ("F", "Žena"), ("O", "Ostatní")],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        default="avatars/default_avatar.webp",
                        null=True,
                        upload_to="avatars/",
                    ),
                ),
                ("birth_date", models.DateField(blank=True, null=True)),
                (
                    "mobile_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
