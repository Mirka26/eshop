# Generated by Django 4.2.7 on 2024-01-23 13:10

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=50)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Muž"), ("F", "Žena"), ("O", "Ostatní")],
                        max_length=1,
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        default="avatars/default_avatar.webp", upload_to="avatars/"
                    ),
                ),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("mobile_number", models.CharField(blank=True, max_length=15)),
                ("address", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]