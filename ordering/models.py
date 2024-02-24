from django.db import models
from paging.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s cart"

class OrderItem(models.Model):
    amount = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self) -> str:
        return f"cart item of {self.cart.user.username}"