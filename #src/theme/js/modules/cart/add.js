import {getCookie} from "../getCookie.js";
import {initCart} from "./cart.js";

export const addCartHandler = (e) => {
  const requestUrl = e.currentTarget.dataset.url;
  const productId = e.currentTarget.dataset.id;
  const csrfToken = getCookie('csrftoken');

  fetch(requestUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    body: JSON.stringify({
      productId: productId
    }),
  })
    .then(response => response.json())
    .then(data => {
      /*const cartItemBody = document.getElementById('cart-item');
      cartItemBody.innerHTML = data.cart_items_html;*/
      document.getElementById("mini-cart_noempty").innerHTML = `
        <h4 class="mini-cart__title">
          Корзина
          <span>(</span>
            <strong id="mini-cart-count">${data.cart_total_count}</strong>
          <span>)</span>
        </h4>
        <div class="mini-cart__inner" id="cart-item">
          {% include "components/cart-item.html" %}
        </div>
        <div class="mini-cart__links">
          <a href="/orders/create/" class="mini-cart__link">Оформить заказ</a>
        </div>`;

      const cartItemsContainer = document.getElementById("cart-item");
      cartItemsContainer.innerHTML = data.cart_items_html;
      initCart();

    })
    .catch(error => console.error(error));
};