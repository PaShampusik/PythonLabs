var banners = document.getElementsByClassName('banner');
var currentIndex = 0;
var intervalId;

function rotateBanners() {
    // Показать следующий баннер
    currentIndex++;
    if (currentIndex >= banners.length) {
        currentIndex = 0;
    }
    banners[currentIndex].classList.add('active');

    // Скрыть текущий баннер
    var previousIndex = currentIndex - 1;
    if (previousIndex < 0) {
        previousIndex = banners.length - 1;
    }
    banners[previousIndex].classList.remove('active');
}

function startRotation() {
    // Запустить ротацию баннеров каждые 5 секунд
    intervalId = setInterval(rotateBanners, 2000);
}

function stopRotation() {
    // Остановить ротацию баннеров
    clearInterval(intervalId);
}

// Проверить наличие фокуса страницы
function checkPageFocus() {
    if (document.hasFocus()) {
        startRotation();
    } else {
        stopRotation();
    }
}

var intervalInput = document.getElementById('interval');

function updateRotationInterval() {
    var newInterval = parseInt(intervalInput.value, 10) * 1000; // Преобразование в миллисекунды
    clearInterval(intervalId);
    intervalId = setInterval(rotateBanners, newInterval);
}
if (intervalInput) {
    intervalInput.addEventListener('change', function () {
        updateRotationInterval();
    });
}

// При загрузке страницы начать ротацию и установить обработчик события изменения фокуса страницы
window.addEventListener('load', function () {
    startRotation();
    window.addEventListener('focus', checkPageFocus);
    window.addEventListener('blur', checkPageFocus);
});