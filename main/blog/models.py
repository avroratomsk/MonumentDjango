from django.db import models
from django.urls import reverse

class BlogSettings(models.Model):
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  description = models.TextField(null=True, blank=True, verbose_name="Текст на странице")

class BlogCategory(models.Model):
  name = models.CharField(max_length=250, db_index=True, verbose_name="Название статьи")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
  description = models.TextField(null=True, blank=True, verbose_name="Текст на странице")
  date_creation = models.DateField(auto_now_add=True)
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  image = models.ImageField(upload_to="blog-category", blank=True, null=True, verbose_name="Изображение статьи")
  updated_at = models.DateTimeField(auto_now=True)  # Поле для даты последнего обновления

  def get_absolute_url(self):
    return reverse("category_post", kwargs={"category_slug": self.slug})

  def __str__(self):
      return self.name

class Post(models.Model):
  STATUS_CHOICES = [
      ('published', 'Опубликовано'),
      ('draft', 'Черновик'),
      ('hidden', 'Скрыто'),
  ]

  name = models.CharField(max_length=250, db_index=True, default='', verbose_name="Название статьи")
  slug = models.SlugField(max_length=200, unique=True, verbose_name="URL")
  description = models.TextField(null=True, blank=True, verbose_name="Содержимое статьи")
  category = models.ForeignKey("BlogCategory", blank=True, null=True, on_delete=models.CASCADE, verbose_name='Категория')
  date_creation = models.DateField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image = models.ImageField(upload_to="blog", verbose_name="Изображение статьи")
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  view_count =  models.PositiveIntegerField(default=0,null=True, blank=True, verbose_name="Счетчик просмотров")
  status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='draft',
    verbose_name="Статус"
  )

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    if self.category:
      return reverse('post', kwargs={
        'category_slug': self.category.slug,
        'slug': self.slug
      })

    return reverse('post_without_category', kwargs={'slug': self.slug})
  