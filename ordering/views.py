from . import models, forms
from cartfav.models import Cart
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index_view(request):
    orders = models.Order.objects.filter(user=request.user)
    return render(request, "ordering/index.html", {"orders": orders})


@login_required
def place_order_view(request):
    if request.method == "POST":
        cart = Cart.objects.get(user=request.user)
        items = cart.cartitem_set.all()

        order = models.Order.objects.create(user=request.user)
        for item in items:
            models.OrderItem.objects.create(
                order=order,
                amount=item.amount,
                product=item.product,
            )
            item.delete()
            cart.shipping_price = 0
            cart.save()
    return redirect("ordering:index")

@login_required
def booking_view(request):
    if request.method == "POST":
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            return redirect("paging:booking")
    
    return redirect("ordering:index")
