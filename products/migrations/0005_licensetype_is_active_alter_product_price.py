# Generated by Django 4.2.20 on 2025-03-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_printtype_remove_product_print_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='licensetype',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
