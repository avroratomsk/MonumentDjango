from django.urls import path

from cart import views

urlpatterns = [
    path('cart-add/', views.cart_add, name="cart_add"),
    path('cart_add-test/', views.cart_add_test, name="cart_add_test"), 
    path('cart_change/', views.cart_change, name="cart_change"), 
    path('cart_remove/', views.cart_remove, name="cart_remove"), 
    path('', views.cart, name="cart"),
]