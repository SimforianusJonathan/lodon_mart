# Generated by Django 5.1.1 on 2024-10-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_product_is_starred'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_starred',
            field=models.BooleanField(default=False),
        ),
    ]
