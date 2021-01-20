'use strict';

let dates = document.querySelectorAll('.list__date');
let status = document.querySelectorAll('.list__status')
for (let ind of dates.keys()){
  let el = dates[ind]
  let s_d = el.textContent.split('.');
  let date = new Date(`${s_d[2]}-${s_d[1]}-${s_d[0]}`);
  let today = new Date();
  let el_status = status[ind];
  if ( (date.getMonth() <= today.getMonth()) && (date.getDate() < today.getDate()) ) {
    el_status.textContent = 'время прошло, ты сделал дз?';
    el_status.classList.add('list__status_skip');
  }
  else if ( ( ( date.getMonth() == today.getMonth() ) || ( (date.getMonth() - today.getMonth()) == 1) ) && ( (date.getDate() - today.getDate()) == 1 ) ){
    el_status.textContent = 'сроки поджимают!!!';
    el_status.classList.add('list__status_tmr');
  }
  else if ( ( date.getMonth() == today.getMonth() ) && ( date.getDate() == today.getDate() ) ) {
    el_status.textContent = 'сдача уже сегодня!!!!!';
    el_status.classList.add('list__status_today');
  }
  else if ( ( ( date.getMonth() == today.getMonth() ) || ( (date.getMonth() - today.getMonth()) == 1) ) && ( (date.getDate() - today.getDate()) < 7 )  ) {
    el_status.textContent = 'осталось меньше недели';
  }
}