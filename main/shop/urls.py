from django.urls import path

from shop import views


urlpatterns = [
    path('search/', views.catalog_search, name="catalog_search"),
    path('', views.category, name="category"),
    path('<slug:slug>/', views.category_detail, name="category_detail"),
    path('<slug:parent>/<slug:slug>/', views.product, name="product"),
    path('<slug:parent>/<slug:product>/<slug:model>/', views.model_detail, name="model_detail"),
]