# Generated by Django 4.1.1 on 2023-05-03 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shirt',
            name='brand',
        ),
    ]
