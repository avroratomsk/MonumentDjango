function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

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
      console.log('Added to cart:', data);
    })
    .catch(error => console.error(error));
};