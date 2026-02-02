import * as functions from './modules/functions.js';

functions.isWebp();

import "./modules/popup/popup.js";
import "./modules/sliders.js";

import Swiper from "swiper";
import {Navigation, Pagination, Scrollbar, Thumbs, EffectFade} from "swiper/modules";

const worksSlider = new Swiper('.works-slider', {
  modules: [Navigation, EffectFade],
  direction: 'horizontal',
  /*effect: 'fade',
  fade: {
    crossFade: true,
  },*/
  autoHeight: true,
  slidesPerView: 3.5,
  spaceBetween: 20,

  navigation: {
    nextEl: '.works-next',
    prevEl: '.works-prev',
  },
});

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


const singleThumb = new Swiper('.single__thumb', {

  direction: 'horizontal',
  loop: true,
  autoHeight: true,
  spaceBetween: 20,
  slidesPerView: 4,

  // scrollbar: {
  //   el: '.swiper-scrollbar',
  //   draggable: true,
  // },

  // breakpoints: {
  //   320: {
  //     scrollbar: {
  //       enabled: true
  //     },
  //     slidesPerView: 1,
  //   },
  //   992: {
  //     slidesPerView: 3,
  //     scrollbar: {
  //       enabled: false
  //     },
  //   }
  // }

});

const singleSlider = new Swiper('.single__slider', {
  modules: {Scrollbar, Pagination},
  direction: 'horizontal',
  loop: true,
  autoHeight: true,
  spaceBetween: 20,

  navigation: {
    nextEl: '.project__slider-next',
    prevEl: '.project__slider-prev',
  },

  scrollbar: {
    el: '.swiper-scrollbar',
    draggable: true,
  },

  thumbs: {
    swiper: singleThumb,
  },

  // breakpoints: {
  //   320: {
  //     scrollbar: {
  //       enabled: true
  //     },
  //     slidesPerView: 1,
  //   },
  //   992: {
  //     slidesPerView: 3,
  //     scrollbar: {
  //       enabled: false
  //     },
  //   }
  // }

});