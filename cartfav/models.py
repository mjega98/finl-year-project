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
        ordering = ["-created_at"]
        unique_together = ["user", "product"]

    def __str__(self) -> str:
        return f"{self.user.username}: {self.product.name.title()}"


class Cart(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    @property
    def sub_total(self):
        return sum([i.total_price for i in self.cartitem_set.all()])

    @property
    def total(self):
        return self.shipping_price + self.sub_total

    def __str__(self) -> str:
        return f"{self.user.username}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product, models.PROTECT)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.product.price * self.amount

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"cart item of {self.cart.user.username}"
