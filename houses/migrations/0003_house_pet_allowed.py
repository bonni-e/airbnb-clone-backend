# Generated by Django 4.2.2 on 2023-06-17 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_rename_price_house_price_per_night'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='pet_allowed',
            field=models.BooleanField(default=True),
        ),
    ]
