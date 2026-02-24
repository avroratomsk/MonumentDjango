import {addCartHandler, closeMiniCartHandler, removeItemCartHandler} from "./index.js";
import {addListener} from "../functions.js";

export const initCart = () => {
  const addCartButtons = document.querySelectorAll('.add-cart-btn');
  addListener(addCartButtons, 'click', addCartHandler);

  const closeCartButtons = document.querySelectorAll('.mini-cart__close');
  addListener(closeCartButtons, 'click', closeMiniCartHandler);

  const miniCartItemRemoveButtons = document.querySelectorAll('.mini-cart__delete');
  addListener(miniCartItemRemoveButtons, 'click', removeItemCartHandler);

  const notification = document.querySelector('.notice');

}