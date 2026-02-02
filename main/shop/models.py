from django.db import models
from django.urls import reverse
import os
from django.conf import settings
from admin.singleton_model import SingletonModel

class ShopSettings(SingletonModel):
  meta_h1 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=250, null=True, blank=True, verbose_name="META заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="META описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="META keywords")
  description = models.TextField(null=True, blank=True,  verbose_name="Текст на странице")


# Категория
class Category(models.Model):
  STATUS_CHOICES = [
    ('published', 'Выводить'),
    ('draft', 'Не выводить'),
    ('hidden', 'Скрыто'),
  ]

  STATUS_VIEW = [
    ('published', 'Выводить'),
    ('draft', 'Не выводить'),
  ]

  name = models.CharField(max_length=150, db_index=True, unique=True, verbose_name="Название категории")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
  description = models.TextField(null=True, blank=True,  verbose_name="Описание категории")
  image = models.ImageField(upload_to="goods/", blank=True, null=True, verbose_name="Изображение категории")
  parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Дочерняя категория")
  meta_h1 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=250, null=True, blank=True, verbose_name="META заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="META описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="META keywords")
  updated_at = models.DateTimeField(auto_now=True)
  order_by = models.CharField(max_length=150, default="0", blank=True, null=True,  db_index=True, verbose_name="Порядок сортировки")
  add_slider = models.CharField(
   max_length=20,
   choices=STATUS_VIEW,
   default='draft',
   verbose_name="Выводить в слайдер ?"
 )
  status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='draft',
    verbose_name="Выводить в каталог ?"
  )
  
  class Meta:
    db_table = 'category' 
    verbose_name = 'Категория'
    verbose_name_plural = "Категории"
    
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("category_detail", kwargs={"slug": self.slug})


class Product(models.Model):
  STATUS_CHOICES = [
    ('published', 'Опубликовано'),
    ('draft', 'Черновик'),
    ('hidden', 'Скрыто'),
  ]

  name = models.CharField(max_length=150, db_index=True, verbose_name="Наименование")
  slug = models.SlugField(max_length=255, unique=True, default="", verbose_name="URL")
  category = models.ManyToManyField(Category, default="", verbose_name="Категории")
  image = models.ImageField(upload_to="product-image/", blank=True, null=True, verbose_name="Изображение товара")
  description = models.TextField(null=True, blank=True,  verbose_name="Описание")
  text = models.TextField(null=True, blank=True,  verbose_name="Текст на странице")
  meta_h1 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=250, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  updated_at = models.DateTimeField(auto_now=True)
  order_by = models.CharField(max_length=150, blank=True, null=True, default="0",  db_index=True, verbose_name="Порядок сортировки")
  status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='draft',
    verbose_name="Статус"
  )

  class Meta:
    db_table = 'product'
    verbose_name = 'Продукт'
    verbose_name_plural = "Продукты"
    ordering = ("-id",)

  def __str__(self):
    return f'{self.name}'

  """ Данный метод добавляет к id нули в начале """
  def display_id(self):
    return f'{self.id:05}' #self.id:05 - сделает так чтобы id состоял из 5 символов, если не хватате символов в начало добавить 0

  """ Данный метод возвращает цену со скидкой"""
  def sell_price(self):
    if self.sale:
      return round(self.price - self.price * self.sale / 100, 2)

    return self.price

  def get_absolute_url(self):
    category = self.category.first()
    return reverse("product", kwargs={"parent": category.slug, "slug": self.slug})



class Models(models.Model):
  STATUS_CHOICES = [
      ('published', 'Опубликовано'),
      ('draft', 'Черновик'),
      ('hidden', 'Скрыто'),
  ]

  STATUS_STOCK = [
        ('published', 'В наличие'),
        ('draft', 'В пути'),
        ('hidden', 'Нет в наличии'),
    ]

  meta_h1 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=250, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  image = models.ImageField(upload_to="model-image/", blank=True, null=True, verbose_name="Изображение модели")
  description = models.TextField(null=True, blank=True,  verbose_name="Описание")
  text = models.TextField(null=True, blank=True,  verbose_name="Текст на странице")
  parent = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True,related_name="models_parent", verbose_name="Продукт")
  slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name="URL")
  model = models.CharField(max_length=150, default="", db_index=True, verbose_name="Модель")
  in_stock = models.CharField(
                   max_length=20,
                   choices=STATUS_STOCK,
                   default='draft',
                   verbose_name="В наличие"
                 )

  status = models.CharField(
      max_length=20,
      choices=STATUS_CHOICES,
      default='draft',
      verbose_name="Статус"
    )

  def get_absolute_url(self):
    product = self.parent
    category = product.category.first()
    return reverse("model_detail", kwargs={
      "parent": category.slug,
      "product": product.slug,
      "model": self.slug
    })

class Characteristic(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class ModelCharacteristic(models.Model):
    model = models.ForeignKey(
      Models,
      on_delete=models.CASCADE,
      related_name="characteristics"
    )
    characteristic = models.ForeignKey(
      Characteristic,
      on_delete=models.CASCADE
    )
    value = models.CharField(max_length=250, null=True, blank=True)

class ProductImage(models.Model):
  parent = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="Привязка к продукту")
  src = models.ImageField(upload_to="product-image/", null=True, blank=True, verbose_name="Дополнительны изображения")

  class Meta:
    verbose_name = 'Изображение'




