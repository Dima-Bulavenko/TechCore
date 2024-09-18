# Generated by Django 5.1 on 2024-09-18 21:38

import django.db.models.deletion
import product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPUProduct',
            fields=[
            ],
            options={
                'verbose_name': 'CPU product',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=(product.models.ProductMixin, 'product.product'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
    ]