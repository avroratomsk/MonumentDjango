import Swiper from "swiper";
import {Navigation, Pagination, Scrollbar, Thumbs, EffectFade} from "swiper/modules";

const worksSlider = new Swiper('.works-slider', {
  modules: [Navigation],
  direction: 'horizontal',
  autoHeight: true,
  spaceBetween: 20,

  navigation: {
    nextEl: '.works-next',
    prevEl: '.works-prev',
  },

  breakpoints: {
    320: {
      slidesPerView: 1,
    },
    480: {
      slidesPerView: 2,
    },
    992: {
      slidesPerView: 3.5,
    }
  }
});

const singleThumb = new Swiper('.single__thumb', {
  modules: [Navigation, Thumbs],
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
  modules: [Scrollbar, Pagination, Thumbs],
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
