# Generated by Django 4.1.1 on 2023-05-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='brand',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
