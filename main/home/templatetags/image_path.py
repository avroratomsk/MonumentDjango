from django import template
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def image_path(image_name):
    return static(f'theme/img/{image_name}')