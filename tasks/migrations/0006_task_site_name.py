# Generated by Django 3.2.6 on 2022-12-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20221226_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='site_name',
            field=models.CharField(default='Krafta', max_length=255),
        ),
    ]
