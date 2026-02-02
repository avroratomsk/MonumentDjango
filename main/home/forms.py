from django import forms
from home.models import HomeTemplate
from shop.models import Category,Product

class CallbackForm(forms.Form):
  name = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваше имя',
      'class': 'form__controls'
      }
  ))

  phone = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваш номер телефона',
      'class': 'form__controls'
      "data-input"
      }
  ))

class OknaForm(forms.Form):
  name = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваше имя',
      'class': 'form__controls'
      }
  ))

  phone = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваш номер телефона',
      'class': 'form__controls'
      "data-input"
      }
  ))
  page_name = forms.CharField(widget=forms.TextInput())

  
  
class ContactForm(forms.Form):
  name = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваше имя',
      'class': 'form__controls'
      }
  ))

  phone = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваш номер телефона',
      'class': 'form__controls'
      "data-input"
      }
  ))
  
  social = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваш номер телефона',
      'class': 'form__controls'
      "data-input"
      }
  ))
  
class OrderForm(forms.Form):
  name = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваше имя',
      'class': 'form__controls'
      }
  ))

  phone = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваш номер телефона',
      'class': 'form__controls'
      "data-input"
      }
  ))
  
  product = forms.CharField()
  
class ConsultationForm(forms.Form):
  name = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваше имя',
      'class': 'form__controls'
      }
  ))

  phone = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваш номер телефона',
      'class': 'form__controls'
      "data-input"
      }
  ))
  
  pagename = forms.CharField()
