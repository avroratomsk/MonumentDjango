from django.urls import path,include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from .sitemap import PostSitemap, ShopCategory, ShopProduct

sitemaps = {
    'posts': PostSitemap,
    'category': ShopCategory,
    'products': ShopProduct,
}

from main import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('category/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('service/', include('service.urls')),
    path('user/', include('users.urls')),
    path('admin/', include('admin.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),  # Маршрут для sitemap.xml
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)