from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post
from shop.models import Category, Product


""" Класс с параметрами sitamp post """
class PostSitemap(Sitemap):
    changefreq = "always"  # Как часто изменяется контент (варианты: 'always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never')
    priority = 0.8  # Приоритет (от 0.0 до 1.0)

    def items(self):
        return Post.objects.filter(status=True).order_by('id')  # Фильтрация объектов, которые будут включены в sitemap

    def lastmod(self, obj):
        return obj.updated_at  # Дата последнего изменения объекта
      

class ShopCategory(Sitemap):
  changefreq = "always"
  priority = 0.8

  def items(self):
      return Category.objects.all().order_by('id')

  def lastmod(self, obj):
      return obj.updated_at
    
class ShopProduct(Sitemap):
  changefreq = "always"
  priority = 0.8

  def items(self):
      return Product.objects.filter(status=True).order_by('id')

  def lastmod(self, obj):
      return obj.updated_at
    
class StaticViewSitemap(Sitemap):
    changefreq = "always"
    priority = 0.8

    def items(self):
        return ['home', 'about', 'contact']  # Здесь перечисли имена URL шаблонов

    def location(self, item):
        return reverse(item)  # Функция reverse генерирует URL по имени шаблона