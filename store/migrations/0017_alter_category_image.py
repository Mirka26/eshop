# Generated by Django 4.2.7 on 2024-01-18 17:38

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[200, 200], upload_to='static/images'),
        ),
    ]
