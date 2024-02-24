from . import models
from paging.models import Product
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def list_cart_view(request):
    cart, _ = models.Cart.objects.get_or_create(user=request.user)
    items = cart.cartitem_set.all()
    return render(request, "cartfav/cart.html", {"items": items})


@login_required
def add_to_cart_view(request, id):
    product = Product.objects.get(id=id)
    cart, _ = models.Cart.objects.get_or_create(user=request.user)
    if request.method == "POST":
        amount = int(request.POST.get("amount", 1))
        cart_item = cart.cartitem_set.filter(product=product).first()
        if cart_item:
            cart_item.amount += amount
            cart_item.save()
        else:
            models.CartItem.objects.create(cart=cart, amount=amount, product=product)
        product.quantity -= amount
        product.save()
    return redirect(request.META.get("HTTP_REFERER", "paging:index"))


@login_required
def remove_from_cart_view(request, id):
    product = Product.objects.get(id=id)
    cart, _ = models.Cart.objects.get_or_create(user=request.user)
    if request.method == "POST":
        cart_item = cart.cartitem_set.filter(product=product).first()
        if cart_item:
            product.quantity += cart_item.amount
            product.save()

            cart_item.delete()
    return redirect(request.META.get("HTTP_REFERER", "paging:index"))


@login_required
def list_favorite_view(request):
    items = models.Favorite.objects.filter(user=request.user)
    return render(request, "cartfav/favorite.html", {"items": items})


@login_required
def add_to_favorite_view(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        fav, _ = models.Favorite.objects.get_or_create(
            product__id=id,
            user=request.user,
            defaults={"user": request.user, "product": product},
        )
        print(fav, _)
    return redirect(request.META.get("HTTP_REFERER", "paging:index"))


@login_required
def remove_from_favorite_view(request, id):
    if request.method == "POST":
        ...
    return redirect(request.META.get("HTTP_REFERER", "paging:index"))
