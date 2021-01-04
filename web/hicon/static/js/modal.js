document.querySelector('.btn_add').addEventListener('click', function(){
  document.querySelector('.overlay').style.display = 'block'
});

document.querySelector('.modal__close').addEventListener('click', function(){
  document.querySelector('.overlay').style.display = 'none'
});