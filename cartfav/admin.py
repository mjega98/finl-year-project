from . import models
from django.contrib import admin


@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin): ...


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin): ...


@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin): ...
