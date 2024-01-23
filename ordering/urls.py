from . import views
from django.urls import path

app_name = "ordering"
urlpatterns = [
    path("", views.index_view, name="index"),
]
