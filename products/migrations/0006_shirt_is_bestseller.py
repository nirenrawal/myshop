# Generated by Django 4.1.1 on 2023-05-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_shirt_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='is_bestseller',
            field=models.BooleanField(default=False),
        ),
    ]
