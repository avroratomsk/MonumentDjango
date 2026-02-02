import {bodyLock, bodyUnLock} from "../functions.js";

const burger = document.querySelector("#burger");
const menuClose = document.querySelector("#menu-close");

export const openMenu = (e) => {
  console.log("openMenu");
  document.querySelector(".nav").classList.add("_active");
  bodyLock();
}

export const closeMenu = (e) => {
  document.querySelector(".nav").classList.remove("_active");
  bodyUnLock();
}

burger?.addEventListener("click", openMenu);
menuClose?.addEventListener("click", closeMenu)
