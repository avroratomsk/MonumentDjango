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
  category = Category.objects.filter(parent=None, status='published')
  slider_category = Category.objects.filter(parent=None, add_slider='published', status='published')
  contact = ContactPage.objects.get()

  context = {
    "settings": settings,
    "slides": slides,
    "category": category,
    "about": about,
    "contact": contact,
    "slider_category": slider_category,
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

  context = {
    "gallery": gallery,
    "items": items,
  }

  return render(request, 'pages/gallery.html', context)


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