import {bodyLock, bodyUnLock} from "../functions.js";

const miniCart = document.getElementById("mini-cart");

export const closeMiniCartHandler = (e) => {
  miniCart.classList.remove("popup_show");
  bodyUnLock();
}