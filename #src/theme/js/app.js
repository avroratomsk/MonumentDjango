import * as functions from './modules/functions.js';

functions.isWebp();

import {Fancybox} from "@fancyapps/ui"

import "./modules/popup/popup.js";
import "./modules/sliders.js";
import "./modules/normalizeFormatPhoneLink.js";
import "./modules/menu/mobileMenu.js";

import { initCart } from './modules/cart/index.js';

document.addEventListener('DOMContentLoaded', () => {
  initCart();
});

Fancybox.bind("[data-fancybox]", {
  // Your custom options
});

import Swiper from "swiper";
import {Navigation, Pagination, Scrollbar, Thumbs, EffectFade} from "swiper/modules";



document.querySelectorAll('.accordion__title').forEach(title => {
  title.addEventListener('click', () => {
    const item = title.parentElement;
    const body = title.nextElementSibling;

    if (item.classList.contains('active')) {
      body.style.maxHeight = body.scrollHeight + 'px';
      requestAnimationFrame(() => body.style.maxHeight = '0');
      item.classList.remove('active');
    } else {
      // закрываем все остальные
      document.querySelectorAll('.accordion__item').forEach(i => {
        i.classList.remove('active');
        i.querySelector('.accordion__body').style.maxHeight = '0';
      });

      item.classList.add('active');
      body.style.maxHeight = body.scrollHeight + 'px';
    }
  });
});