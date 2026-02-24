import {getCookie} from "../getCookie.js";

export const removeItemCartHandler = (e) => {
  const requestUrl = e.currentTarget.dataset.url;
  const cartId = e.currentTarget.dataset.id;
  const csrfToken = getCookie('csrftoken');

  fetch(requestUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    body: JSON.stringify({
      cartId: cartId
    }),
  })
    .then(response => response.json())
    .then(data => {
      const cartItemBody = document.getElementById('cart-item');
      cartItemBody.innerHTML = data.cart_items_html;
    })
    .catch(error => console.error(error));
};