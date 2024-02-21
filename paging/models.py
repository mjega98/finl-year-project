from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name.title()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, models.CASCADE)
    summary = models.CharField(max_length=255, default="")
    image = models.FileField(upload_to="images", default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name.title()
