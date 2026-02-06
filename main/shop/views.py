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
  categories = Category.objects.filter(parent=None, status='published')

  paginator = Paginator(products, 16)
  current_page = paginator.page(int(page))


  context = {
    "categories":categories,
    "settings": settings,
    "products": current_page,
  }

  return render(request, "pages/catalog/category.html", context)
import urllib.parse

def category_detail(request, slug):
  page = request.GET.get("page", 1)
  category = category = get_object_or_404(Category, slug=slug)
  products = Product.objects.filter(status='published', category=category).order_by('order_by')

  if category.children:
    subcategories = Category.objects.filter(parent_id=category)

  context = {
    "subcategories": subcategories,
    "category": category,
    "products": products
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

    if request.method == "POST":
        try:
            result = request.body.decode("utf-8")
            value = json.loads(result).get('value')
            try:
                products = Product.objects.filter(name__icontains=value)
                data = []
                for product in products:

                    try:
                        image  = product.image.url
                    except:
                        image = "/core/theme/mb/images/no-image.png"

                    data.append({
                      'name': product.name,
                      'price': product.price,
                      'url': product.get_absolute_url(),
                      'image': image,
                    })
            except Exception as e:
                print(e)
            return JsonResponse({"value": data})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid JSON'}, status=400)
