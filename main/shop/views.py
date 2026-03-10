from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q
import itertools
from django.db.models import Count
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def category(request):
  try:
    settings = ShopSettings.objects.get()
  except: 
    settings = ShopSettings()

  page = request.GET.get('page', 1)

  products = Product.objects.filter(status='published').order_by('id')
  categories = Category.objects.filter(parent=None, status='published').order_by('order_by')

  paginator = Paginator(products, 16)
  current_page = paginator.page(int(page))


  context = {
    "categories":categories,
    "settings": settings,
    "items": current_page,
  }

  return render(request, "pages/catalog/category.html", context)
import urllib.parse

def category_detail(request, slug):
  page = request.GET.get("page", 1)
  category = get_object_or_404(Category, slug=slug)

  if category.view_all == 'published':
    products = Product.objects.filter(status='published').order_by('-price')
  else:
    products = Product.objects.filter(status='published', category=category).order_by('price')

  if category.children:
    subcategories = Category.objects.filter(parent_id=category).order_by('order_by')


  categories = Category.objects.filter(parent=None, status='published').order_by('order_by')

  paginator = Paginator(products, 16)
  current_page = paginator.page(int(page))

  context = {
    "subcategories": subcategories,
    "categories": categories,
    "category": category,
    "items": current_page
  }

  return render(request, "pages/catalog/category-details.html", context)

def product(request, parent, slug):
    product = Product.objects.get(slug=slug)
    category = Category.objects.get(slug=parent)
    images = ProductImage.objects.filter(parent=product)

    # модели текущего продукта
    models = Models.objects.filter(parent=product)

#     chars = ModelCharacteristic.objects.get(model=models_qs)

    context = {
        "category": category,
        "product": product,
        "images": images,
        "models": models,
    }

    return render(request, "pages/catalog/product.html", context)


def model_detail(request, parent, product, model):
  model = get_object_or_404(Models, slug=model)
  product = Product.objects.get(slug=product)
  category = Category.objects.get(slug=parent)

  context = {
    "category": category,
    "product": product,
    "model": model
  }

  return render(request, "pages/catalog/model.html", context)


@csrf_exempt
def catalog_search(request):
    query = request.GET.get("search", "").strip()

    products = Product.objects.none()
    models = Models.objects.none()
    categories = Category.objects.none()

    if query:
        # Категории
        categories = Category.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query),
            status="published"
        ).distinct()

        # Товары
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query),
            status="published"
        ).prefetch_related("category").distinct()

        # Модели
        models = Models.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query),
            status="published"
        ).select_related("parent").distinct()

    context = {
        "query": query,
        "products": products,
        "models": models,
        "categories": categories,
    }

    return render(request, "pages/catalog/search.html", context)
