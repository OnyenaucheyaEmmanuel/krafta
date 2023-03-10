# Generated by Django 3.2.6 on 2022-12-26 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20221225_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 26, 8, 22, 21, 150176)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 26, 8, 22, 21, 155024)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 26, 8, 22, 21, 149202)),
        ),
    ]
