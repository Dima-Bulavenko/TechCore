# Generated by Django 5.1.1 on 2024-10-26 15:44

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0002_remove_address_phone_number_order_orderlineitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="country",
            field=django_countries.fields.CountryField(
                max_length=100, verbose_name="Country"
            ),
        ),
    ]
