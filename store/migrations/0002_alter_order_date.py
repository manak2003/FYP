# Generated by Django 4.1.1 on 2023-03-28 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 28, 20, 50, 4, 734673)),
        ),
    ]