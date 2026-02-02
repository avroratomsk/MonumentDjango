// document.addEventListener("click", (e) => {
//   const form = document.querySelector(".form--search");
//   if(!form.contains(e.currentTarget)) {
//     console.log('Закрываем')
//   }
// })

const inputSearch = document.querySelector('input[name="catalog-search"]');
inputSearch?.addEventListener("input", (e) => {
  if(e.currentTarget.value !== "") {
    // document.getElementById("search-result").style.display = "none";
    sendDataSearch(e.currentTarget.value);
  }
});

inputSearch?.addEventListener("focusout", (e) => {
  // document.getElementById("search-result").style.display = "none";
})

const searchBtn = document.querySelector("#search-btn");
searchBtn?.addEventListener("click", (e) => {

  e.preventDefault()
  const inputField = e.currentTarget.closest(".form--search")?.querySelector("input[type=search]");
  console.log(inputField)
  if(inputField) {
    const inputvValue = inputField.value.trim();

    if(inputvValue !== "") {
      sendDataSearch(inputvValue);
    }else{
      const productContainer = document.querySelector("#search-result");
      productContainer.style.display = "flex";
      productContainer.innerHTML = `
      <div class="search-result__empty">
        <p>Вы ничего не ввели</p>
      </div>`;
    }
  }else{
    console.error("field not found")
  }
})

async function sendDataSearch(value) {
  try {
    const response = await fetch("/category/search/", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({"value": value}),
    })

    const result = await response.json();
    const productContainer = document.querySelector("#search-result");

    if (response.ok) {
      productContainer.innerHTML = "";
      if (result.value.length) {
        document.getElementById("search-result").style.display = "flex";
        result.value.forEach(item => {
          productContainer.innerHTML += `
          <div class="search-result__item">
            <a href="${item.url}" class="search-result__image">
              <img src="${item.image}" alt="${item.name}">
            </a>
            <a href="${item.url}" class="search-result__link">${item.name}</a>
            <p class="search-result__price">${item.price} ₽</p>
          </div>
      `;
        })
      }else{
        document.getElementById("search-result").style.display = "flex";
        productContainer.innerHTML += `
          <div class="search-result__empty">
            <p>Ничего не найдено</p>
          </div>`
      }
    }
  } catch (error) {
    console.log(`Error sending request: ${value}`);
  }
}

document.getElementById("count")?.addEventListener("change", (e) => {
  const count = e.currentTarget.value;
  window.location.search = `?count=${count}`;
})