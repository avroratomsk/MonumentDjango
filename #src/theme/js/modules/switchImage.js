const colorSwitchBtns = document.querySelectorAll('.color_btn');

const switchImage = (e) => {
  let dataSrc = e.currentTarget.dataset.src;
  let image = document.querySelector('.product-info__image img');
  image.src = dataSrc;
  colorSwitchBtns.forEach(btn => btn.classList.remove('active'));
  e.currentTarget.classList.add('active');
}
colorSwitchBtns.forEach(btn => {
  btn.addEventListener('click', switchImage)
})


