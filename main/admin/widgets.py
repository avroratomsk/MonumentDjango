from django import forms
from django.utils.safestring import mark_safe

class CustomImageWidget(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        html = []
        if value and hasattr(value, "url"):
            html.append(
                f'<div class="form__group form__group-image">'
                f'<label for="id_{name}" class="form__controls-label">Выбор изображения товара :</label>'
                f'На данный момент: <a href="{value.url}">{value.url}</a>'
                f'<input type="checkbox" name="{name}-clear" id="{name}-clear_id">'
                f'<label for="{name}-clear_id">Очистить</label><br>'
                f'Изменить: <input type="file" name="{name}" accept="image/*" id="id_{name}">'
                f'</div>'
            )
        else:
            html.append(super().render(name, value, attrs, renderer))
        return mark_safe("".join(html))