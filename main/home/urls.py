from django.urls import path

from home import views

urlpatterns = [
    path('contact-form/', views.order_form, name="order_form"),
    path('callback-form/', views.callback_form, name="callback_form"),
    path('privacy/', views.privacy, name="privacy"),
    path('cookie/', views.cookie, name="cookie"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('documents/', views.documents, name="documents"),

    path('gallery/', views.gallery, name="gallery"),
    path('<slug:slug>/', views.gallery_detail, name="gallery_detail"),


    path('robots.txt', views.robots_txt),

    path('', views.index, name="home"),
]