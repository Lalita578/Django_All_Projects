# Generated by Django 5.1.3 on 2024-11-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_description_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('laptop', 'Laptop'), ('stationery', 'Stationery'), ('toys', 'Toys')], default='stationery', max_length=20),
        ),
    ]
