# Generated by Django 5.0.1 on 2024-02-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paging", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AddField(
            model_name="product",
            name="summary",
            field=models.CharField(default="", max_length=255),
        ),
    ]
