const slider = new Swiper('.swiper-container', {
  effect: 'fade',
  fadeEffect: {
      crossFade: true
  },
  speed: 800,
  loop: true,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
  },
});