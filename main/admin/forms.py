from django import forms
from home.models import *
from blog.models import *
from service.models import *
from shop.models import *
from branch.models import *
from .widgets import CustomImageWidget
from django_ckeditor_5.widgets import CKEditor5Widget

INPUT_CLASS = "form__controls"

class UploadFileForm(forms.Form):
    file = forms.FileField()

class RobotsForm(forms.ModelForm):
  
  class Meta:
    model = RobotsTxt
    fields = "__all__"
    
    widgets = {'content': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 30 }),}


class ServicePageForm(forms.ModelForm):
  """ Поля настроек старницы услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = ServicePage
    fields = "__all__"
    widgets = {
      'name': forms.TextInput(attrs={
        'class': INPUT_CLASS,
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':INPUT_CLASS,
        "id": "slug"
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_title': forms.TextInput(attrs={
              'class': INPUT_CLASS,
            }),
      'meta_description': forms.Textarea(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': INPUT_CLASS
      })
    }  
    
class ServiceForm(forms.ModelForm):
  """ Form, добавление и редактирование услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Service
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={
        'class': INPUT_CLASS,
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':INPUT_CLASS,
        "id": "slug"
      }),
      'description': forms.Textarea(attrs={
          'class': INPUT_CLASS,
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_title': forms.TextInput(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_description': forms.Textarea(attrs={
        'class': INPUT_CLASS,
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'description':CKEditor5Widget(
         attrs={'class': 'django_ckeditor_5'},
         config_name='extends'
      )
    }


class AutoStyledModelForm(forms.ModelForm):
    DEFAULT_INPUT_CLASS = "form__controls"
    DEFAULT_SELECT_CLASS = "form__controls-select"
    DEFAULT_TEXTAREA_CLASS = "form__controls-textarea",

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        field_styles = {
            forms.CharField: self.DEFAULT_INPUT_CLASS,
            forms.TextInput: self.DEFAULT_INPUT_CLASS,
            forms.EmailInput: self.DEFAULT_INPUT_CLASS,
            forms.NumberInput: self.DEFAULT_INPUT_CLASS,
            forms.DateInput: self.DEFAULT_INPUT_CLASS,
            forms.DateTimeInput: self.DEFAULT_INPUT_CLASS,
            forms.ChoiceField: self.DEFAULT_SELECT_CLASS,
            forms.ModelChoiceField: self.DEFAULT_SELECT_CLASS,
            forms.Textarea: self.DEFAULT_TEXTAREA_CLASS,
            forms.Select: self.DEFAULT_SELECT_CLASS,
        }

        for field_name, field in self.fields.items():
            for widget_type, css_class in field_styles.items():
                if isinstance(field.widget, widget_type) or isinstance(field, widget_type):
                    field.widget.attrs.setdefault('class', css_class)
                    break

# Новые и нужные формы
""" Если нужно добавить дополнительные атрибуты к вставляем вот этот код в класс с создание формы
def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Для TextField добавляем rows
        self.fields['description'].widget.attrs['rows'] = 7
        self.fields['phone'].widget.attrs['placeholder'] = 'Основной телефон'
"""

class GlobalSettingsForm(AutoStyledModelForm):
  class Meta:
    model = BaseSettings
    fields = "__all__"

    widgets = {
      'description':CKEditor5Widget(
          attrs={'class': 'django_ckeditor_5'},
          config_name='extends'
      )
    }

class GalleryPageForm(AutoStyledModelForm):
  class Meta:
    model = GalleryPage
    fields = "__all__"

    widgets = {
      'description':CKEditor5Widget(
          attrs={'class': 'django_ckeditor_5'},
          config_name='extends'
      )
    }

class GalleryItemForm(AutoStyledModelForm):
  class Meta:
    model = GalleryItem
    fields = "__all__"

class SocialsForm(AutoStyledModelForm):
  class Meta:
    model = Socials
    fields = "__all__"

class SliderHeroForm(AutoStyledModelForm):
  class Meta:
    model = SliderHero
    fields = "__all__"

class CallBackBlockForm(AutoStyledModelForm):
  class Meta:
    model = CallBackBlock
    fields = "__all__"

class ModelsForm(AutoStyledModelForm):
  class Meta:
    model = Models
    fields = "__all__"

    widgets = {
      'description':CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      ),
      'text':CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      )
    }

class ClientsForm(AutoStyledModelForm):
  class Meta:
    model = Clients
    fields = "__all__"

class ShopSettingsForm(AutoStyledModelForm):
  class Meta:
      model = ShopSettings
      fields = "__all__"

      widgets = {
        'description':CKEditor5Widget(
          attrs={'class': 'django_ckeditor_5'},
          config_name='extends'
        )
      }

class CategoryForm(AutoStyledModelForm):
  class Meta:
    model = Category
    fields = "__all__"

    widgets = {
      'description':CKEditor5Widget(
          attrs={'class': 'django_ckeditor_5'},
          config_name='extends'
      )
    }

class ProductForm(AutoStyledModelForm):
  class Meta:
    model = Product
    fields = "__all__"

    widgets = {
      'description':CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      ),
      'text':CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      ),
      'category': forms.CheckboxSelectMultiple,
    }

class ProductImageForm(AutoStyledModelForm):
  class Meta:
    model = ProductImage
    fields = "__all__"

    widgets = {
        'src': CustomImageWidget(),
    }

class HomeTemplateForm(AutoStyledModelForm):
  class Meta:
    model = HomeTemplate
    fields = "__all__"

class AboutPageForm(AutoStyledModelForm):
  class Meta:
    model = AboutPage
    fields = "__all__"
    widgets = {
      'description':CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      ),
      'text':CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      ),
    }

class ContactPageForm(AutoStyledModelForm):
  class Meta:
    model = ContactPage
    fields = "__all__"
    widgets = {
      'description':CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      ),
    }

class BlogSettingsForm(AutoStyledModelForm):
  class Meta:
    model = BlogSettings
    fields = "__all__"
    widgets = {
      'description':CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      )
    }

class BlogCategoryForm(AutoStyledModelForm):
  class Meta:
    model = BlogCategory
    fields = "__all__"
    widgets = {
      'description':CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      )

    }

class PostForm(AutoStyledModelForm):
  class Meta:
    model = Post
    fields = "__all__"
    widgets = {
      'description': CKEditor5Widget(
          attrs={'class': 'django_ckeditor_5'},
          config_name='extends'
      )
    }

class BranchForm(AutoStyledModelForm):
  class Meta:
    model = Branch
    fields = "__all__"