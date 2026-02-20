from cart.models import Cart

def user_carts(request):
  user_cart = None
  if request.user.is_authenticated:
      user_cart = Cart.objects.filter(user=request.user).first()
  else:
      session_key = request.session.session_key
      user_cart = Cart.objects.filter(session_key=session_key).first()

  return {'user_cart': user_cart}

