from django import template
from django.utils.http import urlencode
from django.shortcuts import get_object_or_404
from shop.models import Category

register = template.Library()

@register.simple_tag(takes_context=True)
def tag_category():
    return get_object_or_404(Category.objects.all())


@register.simple_tag(takes_context=True)
def chenge_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
