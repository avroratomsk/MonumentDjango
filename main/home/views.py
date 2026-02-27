from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from home.models import *
from home.forms import *
from home.callback_send import email_callback


def index(request):
  try: 
    settings = HomeTemplate.objects.get()

  except:
    settings = HomeTemplate()

  about = AboutPage.objects.first()

  slides = GalleryItem.objects.filter(status='published')
  category = Category.objects.filter(parent=None, status='published')[:4]
  try:
    contact = ContactPage.objects.get()
  except:
    contact = ContactPage()

  context = {
    "settings": settings,
    "slides": slides,
    "category": category,
    "about": about,
    "contact": contact,
  }

  return render(request, 'pages/index.html', context)


def about(request):
  try:
    about = AboutPage.objects.get()
  except:
    about = AboutPage()

  context = {
    "about": about,
  }

  return render(request, 'pages/about.html', context)


def contact(request):
  try:
    contact = ContactPage.objects.get()
  except:
    contact = ContactPage()

  context = {
    "contact": contact,
  }

  return render(request, 'pages/contact.html', context)

def gallery(request):
  try:
    gallery = GalleryPage.objects.get()
  except:
    gallery = GalleryPage()

  items = GalleryItem.objects.filter(status="published")

  category = GalleryCategory.objects.filter(status="published")

  page = request.GET.get('page', 1)
  paginator = Paginator(items, 16)
  current_page = paginator.page(int(page))

  context = {
    "gallery": gallery,
    "items": current_page,
    "categories": category
  }

  return render(request, 'pages/gallery.html', context)

def gallery_detail(request, slug):
  category = GalleryCategory.objects.get(slug=slug)
  categories = GalleryCategory.objects.filter(status="published")
  items = GalleryItem.objects.filter(category__slug=slug, status="published")

  page = request.GET.get('page', 1)
  paginator = Paginator(items, 16)
  current_page = paginator.page(int(page))

  context = {
    "items": current_page,
    "categories": categories,
    "category": category,
  }

  return render(request, 'pages/gallery.html', context)

def documents(request):
  try:
    item = Document.objects.get()
  except:
    item = Document()

  context = {
    "item": item,
  }

  return render(request, 'pages/documents.html', context)


def privacy(request):
  return render(request, "pages/privacy.html")

def cookie(request):
  return render(request, "pages/cookie.html")

def robots_txt(request):
  try:
      robots_txt = RobotsTxt.objects.first()  # Получаем первую запись, т.к. нам нужен только один robots.txt
      content = robots_txt.content if robots_txt else "User-agent: *\nDisallow: /admin/"
  except RobotsTxt.DoesNotExist:
    content = "User-agent: *\nDisallow: /admin/"

  return HttpResponse(content, content_type="text/plain")