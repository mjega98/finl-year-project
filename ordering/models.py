from django.db import models
from paging.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Booking(models.Model):
    ended_at = models.DateTimeField()
    started_at = models.DateTimeField()
    user = models.ForeignKey(User, models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "started_at", "ended_at"]

    def __str__(self) -> str:
        return f"{self.user.username}'s booking on {self.created_at} from {self.started_at} to {self.ended_at}"


class Order(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    @property
    def sub_total(self):
        return sum([i.total_price for i in self.orderitem_set.all()])

    @property
    def total(self):
        return self.shipping_price + self.sub_total

    def __str__(self) -> str:
        return f"{self.user.username}'s order"

class OrderItem(models.Model):
    amount = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)

    @property
    def total_price(self):
        return self.product.price * self.amount

    def __str__(self) -> str:
        return f"order item of {self.order.user.username}"