from . import views
from django.urls import path

app_name = "paging"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("booking/", views.booking_view, name="booking"),
    path("contact-us", views.contact_view, name="contact"),
    path("category/", views.category_view, name="category"),
    path("product/<int:id>/", views.detail_view, name="detail"),
    path("category/<name>/", views.category_view, name="category-filter"),
]
