from django.db import models
from shop.models import Product

from users.models import User

"""Данный класс, считает общую сумму в корзине исходя из product_price()
  product_price() - данный метод находится в таблице Cart
"""
class CartQuerySet(models.QuerySet):
  
  def total_price(self):
    return sum(cart.products_price() for cart in self)
  
  def total_quantity(self):
    if self:
      return sum(cart.quantity for cart in self)
    return 0

"""
  Данная модель создает корзину пользователя,
  но пользователь может быть не авторизован, для этого создано поле session_key
  и корзина сохраняется в сессии и после оформления заказа, мы создаем пользователя из полученных данных при оформлении.
"""
class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Пользователь")
  product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
  quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
  session_key = models.CharField(max_length=32, null=True, blank=True, verbose_name="ключ сессии если пользователь не авторизован")
  created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")
  
  class Meta:
    db_table = "cart"
    verbose_name = "Корзина"
    verbose_name_plural = "Корзины"
    
  objects = CartQuerySet().as_manager()  
        
  def products_price(self):
    return round(self.product.sell_price() * self.quantity, 2)
    
  def __str__(self):
    return self.product.name