# Generated by Django 4.2.7 on 2024-01-17 18:47

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[500, 500], upload_to='static/images/'),
        ),
    ]
