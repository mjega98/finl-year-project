from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name.title()
