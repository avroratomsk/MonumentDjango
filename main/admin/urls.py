from django.urls import path
from . import views

# from .views_new.product_views import admin_product, product_edit, product_add,product_delete


urlpatterns = [
    path('', views.admin, name="admin"),

    # Новые urls
    path('socials/', views.socials, name='socials'),
    path('socials/add/', views.socials_add, name='socials_add'),
    path('socials/<int:pk>/edit/', views.socials_edit, name='socials_edit'),
    path('socials/<int:pk>/delete/', views.socials_delete, name='socials_delete'),

    path('sliders/', views.sliders, name='sliders'),
    path('sliders/add/', views.sliders_add, name='sliders_add'),
    path('sliders/<int:pk>/edit/', views.sliders_edit, name='sliders_edit'),
    path('sliders/<int:pk>/delete/', views.sliders_delete, name='sliders_delete'),

    path('branch/', views.admin_branch, name='admin_branch'),
    path('branch/add/', views.branch_add, name='branch_add'),
    path('branch/<int:pk>/edit/', views.branch_edit, name='branch_edit'),
    path('branch/<int:pk>/delete/', views.branch_delete, name='branch_delete'),

    path('callback-block/', views.admin_callback_block, name='admin_callback_block'),
    path('home-page/', views.admin_home_page, name='admin_home_page'),
    path('about-page/', views.admin_about_page, name='admin_about_page'),
    path('contact-page/', views.admin_contact_page, name='admin_contact_page'),
    path('admin-shop/', views.admin_shop, name='admin_shop'),

    #URl - отвечающие за отображение категорий, редактирование и удаление категории
    path('category/', views.admin_category, name='admin_category'),
    path('category/add/', views.category_add, name='category_add'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),

    path('product/', views.admin_product, name='admin_product'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),

    path('model/', views.admin_model, name='admin_model'),
    path('model/add/', views.model_add, name='model_add'),
    path('model/<int:pk>/edit/', views.model_edit, name='model_edit'),
    path('model/<int:pk>/delete/', views.model_delete, name='model_delete'),

    path('clients/', views.admin_clients, name='admin_clients'),
    path('clients/add/', views.clients_add, name='clients_add'),
    path('clients/<int:pk>/edit/', views.clients_edit, name='clients_edit'),
    path('clients/<int:pk>/delete/', views.clients_delete, name='clients_delete'),

    #URl - отвечающие за отображение категории Страниц блога, редактирование и удаление категории
    path('blog-settings/', views.blog_settings, name='blog_settings'),
    path('post/', views.admin_post, name='admin_post'),
    path('post/add/', views.post_add, name='post_add'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    path('category-blog/', views.category_blog, name='category_blog'),
    path('category-blog/add/', views.category_blog_add, name='category_blog_add'),
    path('category-blog/<int:pk>/edit/', views.category_blog_edit, name='category_blog_edit'),
    path('category-blog/<int:pk>/delete/', views.category_blog_delete, name='category_blog_delete'),


    path('gallery-settings/', views.gallery_settings, name='gallery_settings'),
    path('', views.gallery_add, name='gallery_add'),
    path('gallery/add/gallery/<int:pk>/edit/', views.gallery_edit, name='gallery_edit'),
    path('gallery/<int:pk>/delete/', views.gallery_delete, name='gallery_delete'),

    path('services/', views.admin_services, name='admin_services'),
    path('services/add/', views.services_add, name='services_add'),
    path('services/<int:pk>/edit/', views.services_edit, name='services_edit'),
    path('services/<int:pk>/delete/', views.services_delete, name='services_delete'),

    # Новые конец urls
    
    #URl - отвечающие за загрузку данных
    path('upload-goods/', views.upload_goods, name="upload_goods"),
    path('upload-succes/', views.upload_succes, name="upload-succes"),

    

    #URl - Шаблон общих настроек сайта
    path('settings/', views.admin_settings, name='admin_settings'),
    path('robots/', views.robots, name='robots'),



]