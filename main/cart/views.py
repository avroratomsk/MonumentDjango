from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import redirect, render
from cart.models import Cart
from cart.utils import get_user_carts
from shop.models import Product
import json

def cart(request):
  product_id = request.POST.get("data")
  
  # product = Product.objects.get(id=product_id)
  response_data = {
    'message': 'Привет, мир!',
    'data_received': product_id  # Пример данных, полученных из запроса
  }

  return JsonResponse(response_data)

def cart_add_test(request):
  product_id = request.POST.get("product_id")
  return JsonResponse({"status":"true"})

def cart_add(request):
    data = json.loads(request.body)
    productId = data.get('productId')
    product = Product.objects.get(id=productId)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': 1}
        )
    else:
        session_key = request.session.session_key or request.session.save()
        cart, created = Cart.objects.get_or_create(
            session_key=session_key,
            product=product,
            defaults={'quantity': 1}
        )

    if not created:
        cart.quantity += 1
        cart.save()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string("components/cart-item.html", {"carts": user_cart}, request=request)
    cart_total_count = sum(item.quantity for item in user_cart)

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
        "cart_total_count": cart_total_count
    }
    return JsonResponse(response_data)
  
  
def cart_change(request):
  cart_id = request.POST.get("cart_id")
  quantity = request.POST.get("quantity")

  cart = Cart.objects.get(id=cart_id)

  cart.quantity = quantity
  cart.save()
  updated_quantity = cart.quantity

  cart = get_user_carts(request)
  cart_items_html = render_to_string("components/cart-item.html", {"carts": cart}, request=request)

  response_data = {
      "message": "Количество изменено",
      "cart_items_html": cart_items_html,
      "quaantity": updated_quantity,
  }

  return JsonResponse(response_data)

def cart_remove(request):
    
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string("components/cart-item.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)
