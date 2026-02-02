from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import auth, messages 
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

def login(request):
  field_errors = {}
  if request.method == "POST":
    form = UserLoginForm(data=request.POST)
    if form.is_valid:
      username = request.POST["username"]
      password = request.POST["password"]
      user = auth.authenticate(username=username, password=password)
      session_key = request.session.session_key
      if user:
        auth.login(request, user)
        messages.success(request, f"{username}, Вы вошли в аккаунт")
#
#         if session_key:
#           Cart.objects.filter(session_key=session_key).update(user=user)
        
        """
        Данное условие проверяет если ли ключ next
        Если оно есть, то после авторизации переходим на url после авторизации.
        то есть переходим на ту страницу с которой его редиректнуло
        """
        redirect_page_next = request.POST.get("next", None)
        if redirect_page_next and redirect_page_next != reverse("logout"):
          return HttpResponseRedirect(request.POST.get("next"))
        
        return HttpResponseRedirect(reverse("home"))   
  else:
    form = UserLoginForm()
  
  context = {
    "title": "Страница авторизации",
    "form":form,
  }
  
  return render(request, 'pages/users/login.html', context)

def register(request):
  if request.method == "POST":
    form = UserRegistrationForm(data=request.POST)
    if form.is_valid:
      form.save()
      session_key = request.session.session_key
      user = form.instance
      auth.login(request, user)
#       if session_key:
#         Cart.objects.filter(session_key=session_key).update(user=user)
      messages.success(request, f"{user.username}, Вы успешно зарегистрировались и вошли в аккаунт")
      return HttpResponseRedirect(reverse("home"))
  else:
    form = UserRegistrationForm()
    
  context = {
    "title": "Страница регистрации",
    "form": form
  }
  
  return render(request, 'pages/users/register.html', context)

@login_required
def profile(request):
  if request.method == "POST":
    form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user,)
    if form.is_valid():
      form.save()
      messages.success(request, "Профиль успешно обновлен !")
      return HttpResponseRedirect(reverse("profile"))
  else:
    form = ProfileForm(instance=request.user)
  context = {
    "title": "Личный кабинет",
    "form":form,
  }
  
  return render(request, 'pages/users/profile.html', context)

@login_required
def logout(request):
  messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
  auth.logout(request)
  return redirect(reverse("home"))