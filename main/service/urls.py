from django.urls import path

from service import views


urlpatterns = [
    path('', views.service, name="service"),
    path('<slug:slug>', views.service_detail, name="service_detail"),
    path('okna/', views.service_detail, name="service_detail"),
    path('lodjii/', views.service_detail, name="service_detail"),
]