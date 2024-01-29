# Generated by Django 4.2.7 on 2024-01-17 16:53

from django.db import migrations
import django.utils.timezone
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default=django.utils.timezone.now, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[500, 300], upload_to='whatever'),
            preserve_default=False,
        ),
    ]