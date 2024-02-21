from . import models
from django.shortcuts import render


def index_view(request):
    meals = models.Product.objects.all()[:3]
    return render(request, "paging/index.html", { "meals": meals })


def contact_view(request):
    return render(request, "paging/contact.html")


def category_view(request, name='all'):
    products = models.Product.objects.all()
    categories = models.Category.objects.all()

    if name != 'all':
        products = products.filter(category__name=name)
    return render(request, "category/index.html", {"categories": categories, "products": products})


def detail_view(request, id):
    meal = models.Product.objects.get(id=id)
    return render(request, "paging/product.html", { "meal": meal })
