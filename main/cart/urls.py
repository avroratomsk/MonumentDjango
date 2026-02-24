from django.urls import path

from cart import views

urlpatterns = [
    path('cart-add/', views.cart_add, name="cart_add"),
    path('cart-change/', views.cart_change, name="cart_change"),
    path('cart-remove/', views.cart_remove, name="cart_remove"),
    path('', views.cart, name="cart"),
]