# Generated by Django 5.0.1 on 2024-02-24 22:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ordering", "0001_initial"),
        ("paging", "0003_product_image"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CartItem",
            new_name="OrderItem",
        ),
    ]
