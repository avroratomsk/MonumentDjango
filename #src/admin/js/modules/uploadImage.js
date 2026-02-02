let imageAdd = document.querySelector(".product-block__plus");

imageAdd?.addEventListener("click", () => {
  let image = "<div class=\"product-block__image\"><label for=\"id_src\">Выбрать изображение:</label><input type=\"file\"multiple=\"multiple\"name=\"src\"accept=\"image/*\"required=\"\"id=\"id_src\"><button type='button' class=\"product-block__minus\">Удалить</button></div>";
  document.querySelector(".product-block__paste").innerHTML += image;
});

document.body.addEventListener("click", (e) => {
  if (e.target.classList.contains("product-block__minus")) {
    const parentElement = e.target.closest(".product-block__image");
    parentElement.remove();
  }

});