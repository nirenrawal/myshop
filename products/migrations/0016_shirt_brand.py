# Generated by Django 4.1.1 on 2023-05-03 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_shirt_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand'),
        ),
    ]
