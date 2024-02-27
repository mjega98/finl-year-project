from . import models
from django.contrib import admin


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ["user"]
    list_display = ["user", "started_at", "ended_at", "updated_at", "created_at"]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ["user"]
    list_display = [
        "user",
        "updated_at",
        "created_at",
        "shipping_price",
        "sub_total",
        "total",
    ]


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_filter = ["order"]
    list_display = ["order", "product", "amount", "total_price"]
