from django.shortcuts import render


def index_view(request):
    return render(request, "paging/index.html")


def contact_view(request):
    return render(request, "paging/contact.html")


def category_view(request, name='all'):
    return render(request, "paging/category/index.html")


def detail_view(request, id):
    return render(request, "paging/product.html")
