from home.models import *
from shop.models import Category
from blog.models import BlogCategory
from branch.models import Branch
from service.models import Service

# проверенные функции

def clients(request):
    return {"clients": Clients.objects.filter(status='published')}

def socials(request):
    return {"socials": Socials.objects.filter(status='published')}

def callback_block(request):
    return {"callback": CallBackBlock.load()}
 
def load_settings(request):
    return {'site_settings': BaseSettings.load()}

# проверенные функции

def category(request):
  return {'categories': Category.objects.filter(status='published')}

def branch(request):
    return {"branch": Branch.objects.filter(status='published')}

def category_menu(request):
    return {'category_menu': Category.objects.all()}

def category_blog(request):
    return {'category_blog': BlogCategory.objects.all()}

def services(request):
    return {'services': Service.objects.filter(footer_view=True).order_by('-id')[:4]}


def static_theme_path(request):
    from django.conf import settings
    return {'STATIC_THEME_PATH': settings.STATIC_THEME_PATH}