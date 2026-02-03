from django.core.management.base import BaseCommand
from openpyxl import Workbook
from shop.models import Product

class Command(BaseCommand):
  help = 'Export Product model data to Excel'

  def handle(self, *args, **kwargs):
    wb = Workbook()
    ws = wb.active
    ws.title = 'Products'

    # Заголовки
    headers = [
      'ID', 'Модель', 'Артикл', 'Наименование', 'Slug', 'Категория',
      'Цена', 'Цена со скидкой', 'Полированные стороны', 'Описание',
      'Доставка', 'Изображение', 'Скидка %', 'Количество', 'Вес',
      'Куплено', 'Новинка', 'Опубликован', 'Meta H1', 'Meta Title',
      'Meta Description', 'Meta Keywords', 'Обновлено', 'Вид картинки',
      'В каталоге', 'Сортировка'
    ]
    ws.append(headers)

    # Данные
    for product in Product.objects.all():
      ws.append([
        product.id,
        product.model,
        product.article,
        product.name,
        product.slug,
        product.category.name if product.category else '',
        product.price,
        product.sale_price,
        product.polished_sides,
        product.description,
        product.delivery,
        product.image.url if product.image else '',
        product.discount,
        product.quantity,
        product.weight,
        product.quantity_purchase,
        'Да' if product.latest else 'Нет',
        'Да' if product.status else 'Нет',
        product.meta_h1,
        product.meta_title,
        product.meta_description,
        product.meta_keywords,
        product.updated_at.strftime('%Y-%m-%d %H:%M'),
        'Да' if product.type_image else 'Нет',
        'Да' if product.catalog else 'Нет',
        product.order_by
      ])

    # Сохраняем файл
    file_name = 'products_export.xlsx'
    wb.save(file_name)
    self.stdout.write(self.style.SUCCESS(f'✔ Файл успешно сохранён как "{file_name}"'))