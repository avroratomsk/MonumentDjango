from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate
from users.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
      cleaned_data = super().clean()
      username = cleaned_data.get('username')
      password = cleaned_data.get('password')

      if username and password:
          user = authenticate(username=username, password=password)
          if not user:
              raise forms.ValidationError("Неверное имя пользователя или пароль.")

      return cleaned_data


class UserRegistrationForm(UserCreationForm):
  first_name = forms.CharField()
  last_name = forms.CharField()
  email = forms.CharField()
  username = forms.CharField()
  password1 = forms.CharField()
  password2 = forms.CharField()
  
  class Meta:
    model = User
    fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
    
    
class ProfileForm(UserChangeForm):
  first_name = forms.CharField()
  last_name = forms.CharField()
  email = forms.CharField()
  username = forms.CharField()
  image = forms.ImageField()
  
  class Meta:
    model = User
    fields = ["first_name", "last_name", "username", "email", "image"]
    
 
