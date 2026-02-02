from django.shortcuts import render
from django.shortcuts import render
from news.models import News

def news(request):
  news = News.objects.filter(status=True) 
  
  context = {
    "news": news
  }
  return render(request, "pages/news/news.html", context)


def news_detail(request, slug):
  new = News.objects.get(slug=slug)
  news = News.objects.filter(status=True).exclude(slug=slug)
  context = {
    "new": new,
    "news": news
  }
  return render(request, "pages/news/news_detail.html", context)