from . import views
from django.urls import path

app_name = 'account'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('subscribe/', views.subscribe_view, name='subscribe'),
]