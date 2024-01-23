from . import views
from django.urls import path

app_name = 'paging'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('contact-us', views.contact_view, name='contact'),
    path('category/', views.category_index_view, name='category'),
]