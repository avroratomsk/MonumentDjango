import Swiper from "swiper";
import {Navigation, Pagination, Scrollbar, Thumbs, EffectFade} from "swiper/modules";

const worksSlider = new Swiper('.works-slider', {
  modules: [Navigation],
  direction: 'horizontal',
  autoHeight: true,
  slidesPerView: 4.5,
  spaceBetween: 30,

  navigation: {
    nextEl: '.works-next',
    prevEl: '.works-prev',
  },
});