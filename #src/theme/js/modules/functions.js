/* Проверка поддержки webp, добавление класса webp или no-webp для HTML */
import events from "events";

export function isWebp() {
	// Проверка поддержки webp
	function testWebP(callback) {
		let webP = new Image();
		webP.onload = webP.onerror = function () {
			callback(webP.height == 2);
		};
		webP.src = "data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA";
	}
	// Добавление класса _webp или _no-webp для HTML
	testWebP(function (support) {
		let className = support === true ? 'webp' : 'no-webp';
		document.documentElement.classList.add(className);
	});
}

// Блокировка скролла
export const bodyLock = (e) => {
	let widthScrollBar = window.innerWidth - document.documentElement.clientWidth;

	// document.querySelector('.header').style.marginRight = widthScrollBar + 'px';
	document.documentElement.style.marginRight = widthScrollBar + 'px';
	document.body.classList.add('_lock');
}

// Удаление блокировки скролла
export const bodyUnLock = (e) => {
	document.documentElement.style.marginRight = '0px';
	// document.querySelector('.header').style.marginRight = '0px';
	document.body.classList.remove('_lock');
}