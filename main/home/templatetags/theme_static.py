from django import template
from django.templatetags.static import static

register = template.Library()

@register.simple_tag()
def get_static(file):
    return '/core/theme/mb/' + file
