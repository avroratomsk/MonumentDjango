import {addCartHandler, closeMiniCartHandler, openMiniCartHandler} from "./index.js";

export const initCart = () => {
  const addCartButtons = document.querySelectorAll('.add-cart-btn');

  addCartButtons?.forEach(btn => {
    btn.addEventListener('click', addCartHandler);
  });

  const openCartButtons = document.querySelectorAll('.header__cart');

  openCartButtons?.forEach(btn => {
    btn.addEventListener('click', openMiniCartHandler)
  })

  const closeCartButtons = document.querySelectorAll('.mini-cart__close');

  closeCartButtons?.forEach(btn => {
    btn.addEventListener('click', closeMiniCartHandler)
  })

}