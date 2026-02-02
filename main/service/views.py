from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q

from service.models import Service,ServicePage

def service(request):
  services = Service.objects.filter(status=True)
  try:
    service_settings = ServicePage.objects.get()
  except:
    service_settings = ServicePage()

  print(service_settings)
  
  context = {
    "service_settings": service_settings,
    "services": services
  }
  return render(request, "pages/service/service.html", context)

def service_detail(request, slug):
  service = Service.objects.get(slug=slug)
  
  context = {
    "service": service
  }
  
  return render(request, "pages/service/services.html", context)


def service_new(request):
  return render(request, 'pages/service/service-test.html')


def service_grav(request):
  return render(request, 'pages/service/service_grav.html')

def service_model(request):
  return render(request,  'pages/service/service_model.html')
