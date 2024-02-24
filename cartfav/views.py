from . import models
from django.shortcuts import render


def list_cart_view(request):
    cart, _  = models.Cart.objects.get_or_create(user=request.user)
    items = cart.cartitem_set.all()
    return

def add_to_cart_view(request, id):
    cart, _  = models.Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        carts = cart.cartitem_set.filter(id=id)
        ...
    return

def remove_from_cart_view(request, id):
    cart, _  = models.Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        ...
    return


def list_favorite_view(request):
    return


def add_to_favorite_view(request, id):
    if request.method == 'POST':
        ...
    return


def remove_from_favorite_view(request, id):
    if request.method == 'POST':
        ...
    return