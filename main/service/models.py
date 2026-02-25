from django.db import models
from django.urls import reverse

class ServicePage(models.Model):
  meta_h1 = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета h1")
  description = models.TextField(null=True, blank=True, verbose_name="Описание под заголовком")
  text = models.TextField(null=True, blank=True, verbose_name="Текст на странице")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")

class Service(models.Model):

  STATUS_CHOICES = [
    ('published', 'Опубликовано'),
    ('draft', 'Черновик'),
    ('hidden', 'Скрыто'),
  ]

  STATUS_ACTIVE = [
    ('published', 'Выводить'),
    ('hidden', 'Не выводить'),
  ]

  name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Название услуги")
  slug = models.SlugField(max_length=150, unique=True, verbose_name="URL")
  image = models.ImageField(upload_to="services", blank=True, null=True, verbose_name="Изображение услуги")
  description = models.TextField(null=True, blank=True, verbose_name="Описание")
  text = models.TextField(null=True, blank=True, verbose_name="Текст на странице")
  footer_view = models.BooleanField(default=True, verbose_name="Выводить в футер")
  meta_h1 = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета h1")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")

  status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='draft',
    verbose_name="Статус"
  )
  menu = models.CharField(
      max_length=20,
      choices=STATUS_ACTIVE,
      default='published',
      verbose_name="Выводить в меню"
  )
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("service_detail", kwargs={"slug": self.slug})

class ServiceContent(models.Model):
  parent = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="blocks", verbose_name="Привязка к сервису")
  image = models.ImageField(upload_to="services", blank=True, null=True, verbose_name="Изображение")
  description = models.TextField(null=True, blank=True, verbose_name="Текст")
  
  
  