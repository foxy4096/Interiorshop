from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('clear/', views.clear_cart, name='cart_clear'),
]