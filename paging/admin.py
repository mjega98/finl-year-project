from . import models
from django.contrib import admin


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "quantity", "updated_at", "created_at")
    list_filter = ("category",)
    search_fields = ("name",)


