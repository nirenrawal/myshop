# Generated by Django 4.1.1 on 2023-05-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='suggestions',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]