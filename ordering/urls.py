from . import views
from django.urls import path

app_name = "ordering"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("booking/", views.booking_view, name="booking"),
    path("place-order/", views.place_order_view, name="place-order"),
]
