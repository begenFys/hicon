// устанавливаем значения
'use strict';


if ( localStorage.getItem('show') ) {
  if ( localStorage.show == 0 ) {
    document.querySelector('.overlay').style.display = 'none';
  }
} else {
  localStorage.setItem('show', 0);
}

if ( !localStorage.getItem('pomodoro') ) {
  localStorage.setItem('pomodoro', 0);
  localStorage.setItem('time', 1500);
  localStorage.setItem('relax', 0);
  localStorage.setItem('state', 'Время работы!')
}

// нужные переменные
let pTime = document.querySelector('.pomodoro__time');
let pomo = document.querySelectorAll('.pomodoro__item');
let overlay = document.querySelector('.overlay');
let state = document.querySelector('.pomodoro__state');

// функции
const getMinutes = () => {
  return ("0" + Math.floor(( localStorage.time % 3600 ) / 60)).slice(-2);
}

const getSeconds = () => {
  return ("0" + localStorage.time % 60).slice(-2);
}

const setTime = () => {
  pTime.textContent = `${getMinutes()}:${getSeconds()}`;
}
setTime();

const setState = () => {
  state.textContent = localStorage.state
}
setState();

const pomodoroDone = () => {
  let p = Number(localStorage.pomodoro);
  while (p != 0) {
    p = p - 1;
    pomo[p].classList.add('pomodoro__item_done')
  }
}
if (Number(localStorage.relax)) {
  pomodoroDone();
}

const pomodoroClear = () => {
  let p = Number(localStorage.pomodoro);
  while (p != 0) {
    p = p - 1;
    pomo[p].classList.remove('pomodoro__item_done');
  }
  localStorage.pomodoro = 0;
}

const workTime = () => {
  localStorage.relax = 0;
  localStorage.time = 1500;
  setTime();
  localStorage.state = 'Время работы!'
  setState();
  document.querySelector('.pomodoro__title').textContent = 'Время браться за дело!';
  document.querySelector('.pomodoro__subtitle').textContent = 'Теперь пора вернуться к делам. Погружайся в свои чертоги разума и продолжай работать!';
  overlay.style.display = 'block';
}

const shortRelaxTime = () => {
  localStorage.time = 300;
  localStorage.relax = 1
  setTime();
  localStorage.state = 'Время короткого перерыва!';
  setState();
  document.querySelector('.pomodoro__title').textContent = 'Время короткого перерыва!';
  document.querySelector('.pomodoro__subtitle').textContent = 'Отложи дела в сторону и передохни 5 минут';
  overlay.style.display = 'block';
}

const longRelaxTime = () => {
  localStorage.time = 1800;
  localStorage.relax = 1
  setTime();
  localStorage.state = 'Время длинного перерыва!';
  setState();
  document.querySelector('.pomodoro__title').textContent = 'Время длинного перерыва!';
  document.querySelector('.pomodoro__subtitle').textContent = 'Отложи дела в сторону и передохни 30 минут';
  overlay.style.display = 'block';
}

let countdown;
const startTime = () => {
  countdown = setInterval(function() {
    localStorage.time = localStorage.time - 1;
    if (localStorage.time == 0 && localStorage.pomodoro < 3 && !Number(localStorage.relax)) {
      pauseTime();
      document.querySelector('.pomodoro__audio_done').play();
      shortRelaxTime();
    }
    if (localStorage.time == 0 && Number(localStorage.relax)) {
      pauseTime();
      localStorage.pomodoro = Number(localStorage.pomodoro) + 1;
      pomodoroDone();
      document.querySelector('.pomodoro__audio_work').play();
      workTime();
    }
    if (Number(localStorage.pomodoro) == 3) {
      pomodoroClear();
      document.querySelector('.pomodoro__audio_work').play();
      longRelaxTime();
    }
    setTime();
  }, 1000);
}

const pauseTime = () => {
  window.clearInterval(countdown);
}

const resetTime = () => {
  pauseTime();
  workTime();
}

document.querySelector('.pomodoro__start').addEventListener('click', startTime);
document.querySelector('.pomodoro__pause').addEventListener('click', pauseTime);
document.querySelector('.pomodoro__reset_time').addEventListener('click', resetTime);
document.querySelector('.pomodoro__reset_pomo').addEventListener('click', () => {
  pomodoroClear();
  workTime();
});