# Generated by Django 4.2.7 on 2024-01-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="avatars/default_avatar.webp", upload_to="avatars/"
            ),
        ),
    ]
