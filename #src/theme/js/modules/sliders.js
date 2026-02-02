import Swiper from "swiper";
import {Navigation, Pagination, Scrollbar, Thumbs, EffectFade} from "swiper/modules";

const heroSlider = new Swiper('.hero__slider', {
  modules: [Navigation, EffectFade],
  direction: 'horizontal',
  effect: 'fade',
  fade: {
    crossFade: true,
  },
  autoHeight: true,
  slidesPerView: 1,
  spaceBetween: 20,

  navigation: {
    nextEl: '.hero__arrow-next',
    prevEl: '.hero__arrow-prev',
  },
});

const clientsSlider = new Swiper('.clients__slider', {
  modules: [Navigation, Scrollbar],
  direction: 'horizontal',
  slidesPerView: 4.5,
  spaceBetween: 20,

  navigation: {
    nextEl: '',
    prevEl: '',
  },

  scrollbar: {
    el: '.swiper-scrollbar',
  },
});

const infoSliderThumb = new Swiper('.info__slider-thumb', {
  spaceBetween: 10,
  slidesPerView: 3,

  // scrollbar: {
  //   el: '.swiper-scrollbar',
  //   draggable: true,
  // },

  breakpoints: {
    320: {
      scrollbar: {
        enabled: true
      },
      slidesPerView: 1,
      direction: 'horizontal',
      spaceBetween: 20,
    },
    1200: {
      direction: 'vertical',
      slidesPerView: 3,
      scrollbar: {
        enabled: false
      },
    }
  }

});

const infoSlider = new Swiper('.info__slider', {
  modules: {Scrollbar, Pagination, Thumbs},
  direction: 'horizontal',
  loop: false,
  spaceBetween: 20,
  slidesPerView: 1,

  thumbs: {
    swiper: infoSliderThumb,
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