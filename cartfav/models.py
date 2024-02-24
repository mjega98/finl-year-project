from django.db import models
from paging.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, models.PROTECT)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.user.username}: {self.product.name.title()}"

class Cart(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(Product, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"cart item of {self.cart.user.username}"