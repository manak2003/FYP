# Generated by Django 4.1.1 on 2023-04-07 20:36

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name=store.models.Image),
        ),
    ]
