from django.db import models
from django.urls import reverse

from admin.singleton_model import SingletonModel

class BaseSettings(SingletonModel):
  STATUS_CHOICES = [
    ('published', 'Показывать'),
    ('draft', 'Не показывать'),
  ]

  logo = models.ImageField(upload_to="base-settings/", blank=True, null=True, verbose_name="Логотип")
  logo_dark = models.ImageField(upload_to="base-settings/", blank=True, null=True, verbose_name="Логотип Footer")
  logo_width = models.CharField(max_length=250, blank=True, null=True, db_index=True, verbose_name="Ширина логотипа")
  logo_height = models.CharField(max_length=250, blank=True, null=True, db_index=True, verbose_name="Высота логотипа")
  phone = models.CharField(max_length=50, blank=True, null=True, db_index=True, verbose_name="Основной номер телефона")
  time_work = models.CharField(max_length=250, blank=True, null=True, db_index=True, verbose_name="Время работы")
  time_work_weekend = models.CharField(max_length=250, blank=True, null=True, db_index=True, verbose_name="Время работы в выходные")
  email = models.EmailField(max_length=250, blank=True, null=True, db_index=True, verbose_name="Email")
  address = models.CharField(max_length=250, blank=True, null=True, verbose_name="Адрес")
  city = models.CharField(max_length=250, blank=True, null=True, verbose_name="Город")
  favicon = models.FileField(upload_to='base-settings/', blank=True, null=True, verbose_name="ФавИконка")


class HomeTemplate(SingletonModel):
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.CharField(max_length=350, null=True, blank=True, verbose_name="Meta keywords")
  image = models.ImageField(upload_to="home-page/", blank=True, null=True, verbose_name="Изображение")
  title = models.TextField(max_length=250, blank=True, null=True, verbose_name="Заголовок")
  description = models.TextField(blank=True, null=True, verbose_name="Описание")

class AboutPage(SingletonModel):
  image = models.ImageField(upload_to="about-page/", blank=True, null=True, verbose_name="Изображение")
  title = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок")
  description = models.TextField(blank=True, null=True, verbose_name="Текст справа от картинки")
  text = models.TextField(blank=True, null=True, verbose_name="Текст на странице")
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.CharField(max_length=350, null=True, blank=True, verbose_name="Meta keywords")

class CallBackBlock(SingletonModel):
  image = models.ImageField(upload_to="home-page/", blank=True, null=True, verbose_name="Паттерн")
  title = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок")
  description = models.TextField(blank=True, null=True, verbose_name="Описание")

class Clients(models.Model):
  STATUS_CHOICES = [
    ('published', 'Опубликовано'),
    ('draft', 'Черновик'),
    ('hidden', 'Скрыто'),
  ]

  image = models.ImageField(upload_to="home-page/", default="", verbose_name="Логотип")
  title = models.CharField(max_length=250, default="", verbose_name="Заголовок")
  status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='draft',
    verbose_name="Статус"
  )

class ContactPage(SingletonModel):
  description = models.TextField(blank=True, null=True, verbose_name="Описание")
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.CharField(max_length=350, null=True, blank=True, verbose_name="Meta keywords")
  map_code = models.CharField(max_length=250, blank=True, null=True, verbose_name="Код карты(iframe, script)")
  iin = models.CharField(max_length=250, blank=True, null=True, verbose_name="ИНН")
  ogrn = models.CharField(max_length=250, blank=True, null=True, verbose_name="ОГРН")

class Socials(models.Model):
  STATUS_CHOICES = [
    ('published', 'Опубликовано'),
    ('draft', 'Черновик'),
    ('hidden', 'Скрыто'),
  ]

  name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Название соц.сети")
  icon_white = models.FileField(upload_to="icons/", blank=True, null=True, verbose_name="Иконка светлая")
  icon_dark = models.FileField(upload_to="icons/", blank=True, null=True, verbose_name="Иконка темная")
  link = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка")
  status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='draft',
    verbose_name="Статус"
  )

class SliderHero(models.Model):
  STATUS_CHOICES = [
    ('published', 'Опубликовано'),
    ('draft', 'Черновик'),
    ('hidden', 'Скрыто'),
  ]

  title = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок")
  description = models.TextField(blank=True, null=True, verbose_name="Описание")
  image = models.ImageField(upload_to="sliders/", blank=True, null=True, verbose_name="Изображение")
  link = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка")
  status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='draft',
    verbose_name="Статус"
  )

class GalleryPage(SingletonModel):
  title = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок")
  description = models.TextField(blank=True, null=True, verbose_name="Текст на странице")
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.CharField(max_length=350, null=True, blank=True, verbose_name="Meta keywords")

class GalleryItem(models.Model):
  STATUS_CHOICES = [
      ('published', 'Опубликовано'),
      ('draft', 'Черновик'),
      ('hidden', 'Скрыто'),
  ]
  title = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок(alt/title)")
  image = models.ImageField(upload_to="gallery/", blank=True, null=True, verbose_name="Изображение")
  status = models.CharField(
      max_length=20,
      choices=STATUS_CHOICES,
      default='draft',
      verbose_name="Статус"
  )


class RobotsTxt(models.Model):
  content = models.TextField(default="User-agent: *\nDisallow: /admin/")
    
  def __str__(self):
    return "robots.txt"

