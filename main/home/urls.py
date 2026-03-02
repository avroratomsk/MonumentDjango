from django.urls import path

from home import views

urlpatterns = [
    path('privacy/', views.privacy, name="privacy"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('documents/', views.documents, name="documents"),
    path('gallery/', views.gallery, name="gallery"),
    path('<slug:slug>/', views.gallery_detail, name="gallery_detail"),
    path('cookie/', views.cookie, name="cookie"),
    path('robots.txt', views.robots_txt),

    path('', views.index, name="home"),
]