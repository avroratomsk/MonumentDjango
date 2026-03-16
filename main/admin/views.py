import math
import os
import zipfile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from admin.forms import *
from home.models import *
from blog.models import *
from branch.models import *
from main.settings import BASE_DIR
from service.models import *
from shop.models import *
from .utils.views import *


from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
import openpyxl
import pandas as pd
from django.core.files.images import ImageFile
from django.contrib.auth.decorators import user_passes_test
import uuid
import numpy as np
import math
from pytils.translit import slugify
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
import logging
logger = logging.getLogger(__name__)

# from slugify import slugify
# from django.utils.text import slugify
general_url_product = "/admin/product/"

path = f"{BASE_DIR}/upload/upload.zip"
path_to_excel = f"{BASE_DIR}/upload/upload.xlsx"
images_folder = f"{BASE_DIR}/upload/image"
folder = 'upload/'


from django.conf import settings
from PIL import Image as PILImage
from django.core.files.base import ContentFile

def unzip_archive():
  with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall()


def get_unique_slug(model, base_slug):
    slug = base_slug
    counter = 1
    while model.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug

def parse_excel_column(value):
    """ Превращает ячейку Excel в список значений.
        Пустые ячейки -> [''] (одно пустое значение) """
    if pd.isna(value) or value is None:
        return [''], True  # как список

    # Делаем строки и разделяем
    items = [x.strip() for x in str(value).split(',')]
    # Если после очистки пусто → одно пустое значение
    if not any(items):
        return [''], True

    return items, True

def get_value(values, index, total_count):
    # Если список пустой — вернуть пустую строку
    if not values:
        return ""

    # Если одно значение — использовать его для всех
    if len(values) == 1:
        return values[0]

    # Если значений много — использовать по индексу (если хватает)
    if index < len(values):
        return values[index]

    # Если значений меньше чем моделей — пусто
    return ""

import unicodedata
def rename_image(filename):
    if not filename or pd.isna(filename):
        return ""

    try:
        original_name = unicodedata.normalize("NFKC", str(filename)).strip()
        image_name, ext = os.path.splitext(original_name)
        ext = ext.lower()

        slug_name = slugify(image_name)
        if not slug_name:
            slug_name = "image"

        new_filename = f"{slug_name}{ext}"

        old_path = os.path.join(images_folder, original_name)
        new_path = os.path.join(images_folder, new_filename)

        if os.path.exists(new_path):
            return f"goods/{new_filename}"

        if os.path.exists(old_path):
            os.rename(old_path, new_path)
        else:
          pass
#             print(f"ФАЙЛ НЕ НАЙДЕН: {old_path}")

        return f"goods/{new_filename}"

    except Exception as e:
#         print(f"Ошибка rename_image({filename}): {e}")
        return ""

from decimal import Decimal
def import_products_from_excel(file_path):
#   Product.objects.all().delete()
#   Category.objects.all().delete()
#   Models.objects.all().delete()

  df = pd.read_excel(file_path, engine='openpyxl')

  FIXED_COLUMNS_COUNT = 7

  for _, row in df.iterrows():

    parent_raw = row.iloc[17]

    if pd.isna(parent_raw):
      parent_category_name = None
    else:
      parent_category_name = str(parent_raw).strip()

    parent_category_slug = slugify(parent_category_name)

    category_parent = None

    if parent_category_name:
      parent_category_slug = slugify(parent_category_name)

      category_parent, created = Category.objects.get_or_create(
          name=parent_category_name,
          defaults={
              'slug': parent_category_slug,
              'status': 'published',
          }
      )

    category_name = str(row.iloc[0]).strip()
    if not category_name:
        continue

#         image = rename_image(row.iloc[3])
    order_by_category = row.iloc[15]
    category_image = f'goods/{row.iloc[18]}'
    category_slug = slugify(category_name)
    category, created = Category.objects.get_or_create(
        name=category_name,
        defaults={
            'slug': category_slug,
            'parent': category_parent,
            'status': 'published',
            'order_by': order_by_category,
            'image': category_image,
        }
    )

    product_name = str(row.iloc[1]).strip()

    if not product_name:
        continue

    model_raw = row.iloc[2]

    if pd.isna(model_raw):
        model = None
    else:
        model = str(model_raw).strip()

    product_image = f'goods/{row.iloc[3]}'

    product_slug = slugify(product_name)
    product_unique_slug = get_unique_slug(Product, product_slug)

    price_raw = row.iloc[4]

    if pd.isna(price_raw) or str(price_raw).lower() == "nan":
        price = None
    else:
        price = Decimal(str(price_raw))

    order_by_product = row.iloc[16]


    product, pr_created = Product.objects.get_or_create(
        slug=product_unique_slug,
        defaults={
          'name': product_name,
          'price': price,
          'status': 'published',
          'image': product_image,
          'model': model,
          'order_by': order_by_product
        }
    )

    if not pr_created:
      if product_image:
        product.image = product_image
      product.save(update_fields=['image'])

    product.category.add(category)



# @user_passes_test(lambda u: u.is_superuser)
import urllib.parse

@user_passes_test(lambda u: u.is_superuser)
def admin(request):
#   import_products_from_excel(path_to_excel)

  # unzip_archive()
  """Данная предстовление отобразает главную страницу админ панели"""
  return render(request, "page/index.html")

@user_passes_test(lambda u: u.is_superuser)
def robots(request):
  try:
    robots = RobotsTxt.objects.get()
  except:
    robots = RobotsTxt()
    robots.save()

  if request.method == "POST":
    form_new = RobotsForm(request.POST, request.FILES, instance=robots)
    if form_new.is_valid():
      form_new.save()

      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "settings/robots.html", {"form": form_new})

  robots = RobotsTxt.objects.get()

  form = RobotsForm(instance=robots)

  context = {
    "form": form,
    "robots":robots
  }

  return render(request, "settings/robots.html", context)

folder = 'upload/'

from PIL import Image

@user_passes_test(lambda u: u.is_superuser)
def upload_goods(request):
    form = UploadFileForm()

    if request.method == 'POST':
      form = UploadFileForm(request.POST, request.FILES)
      if form.is_valid():
        file = request.FILES['file']
#         import_products_from_excel(file)

#         destination = open(os.path.join('upload/', file.name), 'wb+')
#
#         for chunk in file.chunks():
#           destination.write(chunk)
#         destination.close()
#
#         # Распаковка архива
#         with zipfile.ZipFile(f'upload/{file}', 'r') as zip_ref:
#             zip_ref.extractall('media/')
#
#         # Удаление загруженного архива
#         os.remove(f'upload/{file}')
#
#         # Сжатие фотографий
#         for filename in os.listdir('media/upload'):
#
#           if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.JPG') or filename.endswith('.JPEG') or filename.endswith('.jpeg'):
#             with Image.open(os.path.join('media/upload', filename)) as img:
#               temp = filename.replace('.jpeg', '')
#               temp_one = temp.replace('№', '')
#               temp_b = temp_one.replace('В', 'B')
#               temp_e = temp_one.replace('Э', 'E')
#               img.save(os.path.join('media/goods', temp_e), quality=60)  # quality=60 для JPEG файла
#
#         # Очистка временной папки
#         os.system('rm -rf media/upload')
#         return redirect('upload-succes')
#       else:
#         form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def upload_succes(request):
  return render(request, "upload/upload-succes.html")

# Новые views

""" Общие настройки сайта """
@user_passes_test(lambda u: u.is_superuser)
def admin_settings(request):
  return generic_singleton_edit(request, GlobalSettingsForm, BaseSettings, "Общие настройки", template_name=None)


""" Социальные сети """
@user_passes_test(lambda u: u.is_superuser)
def socials(request):
    return generic_list(request, Socials, "Соц.сети", "socials_add", "socials_edit", "socials_delete")

@user_passes_test(lambda u: u.is_superuser)
def socials_add(request):
    return generic_add(request, SocialsForm, "socials", "Добавление соц.сети",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def socials_edit(request, pk):
  return generic_edit(request, pk, Socials, SocialsForm, "socials", "Редактирование соц.сети",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def socials_delete(request, pk):
    return generic_delete(request, Socials, pk)


""" Слайдеры """

@user_passes_test(lambda u: u.is_superuser)
def sliders(request):
    return generic_list(request, SliderHero, "Слайдер", "sliders_add", "sliders_edit", "sliders_delete")

@user_passes_test(lambda u: u.is_superuser)
def sliders_add(request):
    return generic_add(request, SliderHeroForm, "sliders", "Добавление слайда",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def sliders_edit(request, pk):
  return generic_edit(  request,  pk, SliderHero,  SliderHeroForm, "sliders", "Редактирование слайда", template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def sliders_delete(request, pk):
    return generic_delete(request, SliderHero, pk)


""" Филиалы """
@user_passes_test(lambda u: u.is_superuser)
def admin_branch(request):
  return generic_list(request, Branch, "Филиалы", "branch_add", "branch_edit", "branch_delete")

@user_passes_test(lambda u: u.is_superuser)
def branch_add(request):
  return generic_add(request, BranchForm, "admin_branch", "Добавление Филиала",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def branch_edit(request, pk):
  return generic_edit(  request,  pk, Branch,  BranchForm, "admin_branch", "Редактирование Филиала", template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def branch_delete(request, pk):
  return generic_delete(request, Branch, pk)


""" Блок callback на главной странице """
@user_passes_test(lambda u: u.is_superuser)
def admin_callback_block(request):
  return generic_singleton_edit(request, CallBackBlockForm, CallBackBlock, "Настройки блока", template_name=None)


""" Настройки главной страницы """
@user_passes_test(lambda u: u.is_superuser)
def admin_home_page(request):
  return generic_singleton_edit(request,
  HomeTemplateForm,
  HomeTemplate,
  "Настройки главной страницы",
  template_name="common-template/singleton_page_edit.html"
  )


""" Настройки страницы о нас """
@user_passes_test(lambda u: u.is_superuser)
def admin_about_page(request):
  return generic_singleton_edit(request, AboutPageForm, AboutPage, "Настройки страницы о нас", template_name=None)


""" Настройки страницы о нас """
@user_passes_test(lambda u: u.is_superuser)
def admin_contact_page(request):
  return generic_singleton_edit(request, ContactPageForm, ContactPage, "Настройки страницы контакты", template_name=None)


""" Настройки страницы блога """
@user_passes_test(lambda u: u.is_superuser)
def blog_settings(request, **extra_context):
    try:
      instance = BlogSettings.objects.get()
      items = Post.objects.all()
      category = BlogCategory.objects.all()
    except BlogSettings.DoesNotExist:
      instance = BlogSettings()
      items = Post()
      category = BlogCategory()
      instance.save()
    except Exception as e:
      messages.error(request, f"Ошибка: {e}")
      return redirect(request.META.get('HTTP_REFERER'))

    if request.method == "POST":
      form = BlogSettingsForm(request.POST, request.FILES, instance=instance)

      if form.is_valid():
        try:
          saved_instance = form.save()
          messages.success(request, "Успешно сохранено!")
          return redirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
          messages.error(request, f"Ошибка сохранения: {e}")
      else:
        return render(request, "common-template/generic_page_editor.html", {
          "form": form,
          "title": "Настройки блога",
          "settings": instance,
          "items": items,
          "category": category,
          "edit_url": "post_edit",
          "delete_url": "post_delete",
        })

    form = BlogSettingsForm(instance=instance)

    context = {
      "form": form,
      "title": "Настройки блога",
      "settings": instance,
      "items": items,
      "add_url": "post_add",
      "edit_url": "post_edit",
      "delete_url": "post_delete"
    }

    return render(request,"common-template/generic_page_editor.html", context)


""" Категории товаров """
@user_passes_test(lambda u: u.is_superuser)
def admin_category(request):
  return generic_list(request, Category, "Категории", "category_add", "category_edit", "category_delete")

@user_passes_test(lambda u: u.is_superuser)
def category_add(request):
  return generic_add(request, CategoryForm, "admin_category", "Добавление категории",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def category_edit(request, pk):
  return generic_edit(  request,  pk, Category,  CategoryForm, "admin_category", "Редактирование категории", template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
  return generic_delete(request, Category, pk)


""" Настройки страницы каталога """
@user_passes_test(lambda u: u.is_superuser)
def admin_shop(request):
  return generic_singleton_edit(
  request,
  ShopSettingsForm,
  ShopSettings,
  "Настройки страницы каталога",
  template_name="common-template/singleton_page_edit.html",
  )

""" Товары """
@user_passes_test(lambda u: u.is_superuser)
def admin_product(request):
  return generic_list(request, Product, "Товары", "product_add", "product_edit", "product_delete")

@user_passes_test(lambda u: u.is_superuser)
def product_edit(request, pk):
  """
    View, которая получает данные из формы редактирования товара
    и изменяет данные внесенные данные товара в базе данных
  """
  product = Product.objects.get(id=pk)
  images = ProductImage.objects.filter(parent_id=pk)
  models = Models.objects.filter(parent_id=pk)
  form = ProductForm(instance=product)
  form_new = ProductForm(request.POST, request.FILES, instance=product)

  if request.method == 'POST':
    if form_new.is_valid():
      form_new.save()
      product = Product.objects.get(id=pk)
      images = request.FILES.getlist('src')

      for image in images:
        img = ProductImage(parent=product, src=image)
        img.save()

      messages.success(request, "Успешно сохранено !")
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      error_list = []

      for field_name, errors in form.errors.items():
        if field_name == "__all__":
          for error in errors:
            error_list.append(error)
          continue
        field_label = form[field_name].label

        for error in errors:
          error_list.append(f"{field_label}: {error}")
      messages.error(request, " | ".join(error_list))
      return render(request, 'common-template/product-edit-add-page.html', {'form': form_new})

  context = {
    "form": form,
    "title": "Страница редактирования",
    "url": general_url_product,
    "images": images,
  }

  return render(request, "common-template/product-edit-add-page.html", context)

@user_passes_test(lambda u: u.is_superuser)
def product_add(request):
  return generic_add(request, ProductForm, "admin_shop", "Добавление Товара",  template_name="common-template/product-edit-add-page.html")

@user_passes_test(lambda u: u.is_superuser)
def product_delete(request,pk):
  return generic_delete(request, Product, pk)


""" Модели товаров """
@user_passes_test(lambda u: u.is_superuser)
def admin_model(request):
  return generic_list(request, Models, "Модели", "model_add", "model_edit", "model_delete")

@user_passes_test(lambda u: u.is_superuser)
def model_add(request):
  return generic_add(request, ModelsForm, "admin_model", "Добавление модели",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def model_edit(request, pk):
  return generic_edit(  request,  pk, Models,  ModelsForm, "admin_model", "Редактирование модели", template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def model_delete(request, pk):
  return generic_delete(request, Models, pk)


""" Наши клиенты блок """
@user_passes_test(lambda u: u.is_superuser)
def admin_clients(request):
  return generic_list(request, Clients, "Наши клиенты", "clients_add", "clients_edit", "clients_delete")

@user_passes_test(lambda u: u.is_superuser)
def clients_add(request):
  return generic_add(request, ClientsForm, "admin_clients", "Добавление блока",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def clients_edit(request, pk):
  return generic_edit(  request,  pk, Clients,  ClientsForm, "admin_clients", "Редактирование блока", template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def clients_delete(request, pk):
  return generic_delete(request, Clients, pk)


""" Настройки блога """
@user_passes_test(lambda u: u.is_superuser)
def admin_post(request):
  return generic_list(request, Post, "Статьи", "post_add", "post_edit", "post_delete")

@user_passes_test(lambda u: u.is_superuser)
def post_add(request):
  return generic_add(request, PostForm, "admin_post", "Добавление статьи",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def post_edit(request, pk):
  return generic_edit(  request,  pk, Post,  PostForm, "admin_post", "Редактирование статьи", template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def post_delete(request, pk):
  return generic_delete(request, Post, pk)


""" Настройки категорий блога """
@user_passes_test(lambda u: u.is_superuser)
def category_blog(request):
  return generic_list(request, BlogCategory, "Категории статей", "category_blog_add", "category_blog_edit", "category_blog_delete")

@user_passes_test(lambda u: u.is_superuser)
def category_blog_add(request):
  return generic_add(request, BlogCategoryForm, "category_blog", "Добавление категории статей",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def category_blog_edit(request, pk):
  return generic_edit(request,  pk, BlogCategory,  BlogCategoryForm, "category_blog", "Редактирование категории статей", template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def category_blog_delete(request, pk):
  return generic_delete(request, BlogCategory, pk)

""" Настройки Документы """
@user_passes_test(lambda u: u.is_superuser)
def docs_settings(request):
  return generic_singleton_edit(request, DocumentForm, Document, "Настройки страницы документы", template_name="common-template/singleton_page_edit.html")

@user_passes_test(lambda u: u.is_superuser)
def docs_list(request):
  return generic_list(request, DocumentItem, "Добавление документов", "docs_add", "docs_edit", "docs_delete")

@user_passes_test(lambda u: u.is_superuser)
def docs_add(request):
  return generic_add(request, DocumentItemForm, "docs_settings", "Добавление документов",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def docs_edit(request, pk):
  return generic_edit(request,  pk, DocumentItem,  DocumentItemForm, "docs_settings", "Редактирование фотографии", template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def docs_delete(request, pk):
  return generic_delete(request, DocumentItem, pk)

""" Настройки Галереи """
@user_passes_test(lambda u: u.is_superuser)
def gallery_settings(request):
  return generic_singleton_edit(request, GalleryPageForm, GalleryPage, "Настройки страницы галерея", template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def gallery_list(request):
  return generic_list(request, GalleryItem, "Добавление фотографии", "gallery_add", "gallery_edit", "gallery_delete")

@user_passes_test(lambda u: u.is_superuser)
def gallery_add(request):
  return generic_add(request, GalleryItemForm, "gallery_settings", "Добавление фотографии",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def gallery_edit(request, pk):
  return generic_edit(request,  pk, GalleryItem,  GalleryItemForm, "gallery_settings", "Редактирование фотографии", template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def gallery_delete(request, pk):
  return generic_delete(request, GalleryItem, pk)

@user_passes_test(lambda u: u.is_superuser)
def gallery_category_list(request):
  return generic_list(request, GalleryCategory, "Список категорий", "gallery_category_add", "gallery_category_edit", "gallery_category_delete")

@user_passes_test(lambda u: u.is_superuser)
def gallery_category_add(request):
  return generic_add(request, GalleryCategoryForm, "gallery_category_list", "Добавление категории фотографий",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def gallery_category_edit(request, pk):
  return generic_edit(request,  pk, GalleryCategory,  GalleryCategoryForm, "gallery_category_list", "Редактирование категории фотографий", template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def gallery_category_delete(request, pk):
  return generic_delete(request, GalleryCategory, pk)


""" Настройки услуг """
@user_passes_test(lambda u: u.is_superuser)
def admin_services(request):
  return generic_singleton_edit(request, ServicePageForm, ServicePage, "Настройки страницы Услуг", template_name="common-template/singleton_page_edit.html")

@user_passes_test(lambda u: u.is_superuser)
def services(request):
  return generic_list(request, Service, "Услуги", "services_add", "services_edit", "services_delete")

@user_passes_test(lambda u: u.is_superuser)
def services_add(request):
  return generic_add(request, ServiceForm, "services", "Добавление услуги",  template_name=None)

@user_passes_test(lambda u: u.is_superuser)
def services_edit(request, pk):
  service = Service.objects.get(id=pk)
  blocks = ServiceContent.objects.filter(parent=service)

  if request.method == 'POST':
    form = ServiceForm(request.POST, request.FILES, instance=service)

    if form.is_valid():
      service = form.save()

      # получаем массивы
      descriptions = request.POST.getlist('block_description[]')
      images = request.FILES.getlist('block_image[]')

      for i in range(len(descriptions)):
        description = descriptions[i]
        image = images[i] if i < len(images) else None

        if description or image:
          ServiceContent.objects.create(
            parent=service,
            description=description,
            image=image
          )

      messages.success(request, "Успешно сохранено!")
      return redirect(request.META.get('HTTP_REFERER'))

    else:
      messages.error(request, "Ошибка формы")

  else:
    form = ServiceForm(instance=service)

  context = {
    "form": form,
    "title": "Страница редактирования",
    "block": blocks,
  }

  return render(request, "common-template/product-edit-add-page.html", context)

@user_passes_test(lambda u: u.is_superuser)
def services_delete(request, pk):
  return generic_delete(request, Service, pk)


def upload_archive(request):
  if request.method == 'POST':
    form = ArchiveUploadForm(request.POST, request.FILES)

    if form.is_valid():
      category = form.cleaned_data['category']
      archive = form.cleaned_data['archive']

      GalleryItem.objects.filter(category=category).delete()

      temp_dir = os.path.join(settings.MEDIA_ROOT, 'gallery-image')
      os.makedirs(temp_dir, exist_ok=True)

      with zipfile.ZipFile(archive, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

      # Обрабатываем каждый файл в директории
      for root, dirs, files in os.walk(temp_dir):
        for file in files:
          file_path = os.path.join(root, file)

          try:
            img = PILImage.open(file_path)
            img.verify()
            relative_path = os.path.relpath(file_path, settings.MEDIA_ROOT)
            new_image = GalleryItem.objects.create(
              image=relative_path,
              category=category,
              status='published'
            )
          except (PILImage.UnidentifiedImageError, PILImage.DecompressionBombError):
            continue

      return redirect('gallery')
  else:
    form = ArchiveUploadForm()

  return render(request, 'common-template/upload_archive.html', {'form': form})

