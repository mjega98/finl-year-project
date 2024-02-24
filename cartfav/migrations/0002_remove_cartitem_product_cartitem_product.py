# Generated by Django 5.0.1 on 2024-02-24 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cartfav", "0001_initial"),
        ("paging", "0003_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="product",
        ),
        migrations.AddField(
            model_name="cartitem",
            name="product",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="paging.product",
            ),
            preserve_default=False,
        ),
    ]
