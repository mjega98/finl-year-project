from . import views
from django.urls import path

app_name = "cartfav"
urlpatterns = [
    path("cart/", views.list_cart_view, name="cart"),
    path("favorite/", views.list_favorite_view, name="favorite"),
    path("add-to-cart/<int:id>/", views.add_to_cart_view, name="add-to-cart"),
    path("add-to-favorite/<int:id>/", views.add_to_favorite_view, name="add-to-favorite"),
    path("remove-from-cart/<int:id>/", views.remove_from_cart_view, name="remove-from-cart"),
    path("remove-from-favorite/<int:id>/", views.remove_from_favorite_view, name="remove-from-favorite"),
]
