# Generated by Django 4.2.7 on 2024-01-25 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0003_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={},
        ),
        migrations.AlterModelManagers(
            name="profile",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="profile",
            name="user_ptr",
        ),
        migrations.AddField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
