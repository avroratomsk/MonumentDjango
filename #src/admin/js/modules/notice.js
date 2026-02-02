const notices = document.querySelectorAll('.notice');

notices.forEach(function (notice) {
    // Автоскрытие через 5 секунд
    setTimeout(function () {
        notice.style.opacity = '0';
        notice.style.transition = 'opacity 0.5s ease';

        // Удаление из DOM после анимации
        setTimeout(function () {
            notice.remove();
        }, 300);

    }, 3000);

    // Закрытие по клику (опционально)
    notice.addEventListener('click', function () {
        this.style.opacity = '0';
        setTimeout(() => this.remove(), 500);
    });
});
