var itemImages = document.getElementsByClassName('item-image');

// Функция для применения вращения к фотографии
function rotateImage(image) {
    var rotation = parseInt(image.getAttribute('data-rotation'));
    rotation += 5; // Измените значение угла поворота по вашему усмотрению
    image.style.transform = 'rotate(' + rotation + 'deg)';
    image.setAttribute('data-rotation', rotation);
}

// Функция для обработки скроллинга страницы
function handleScroll() {
    for (var i = 0; i < itemImages.length; i++) {
        var image = itemImages[i];
        var rect = image.getBoundingClientRect();
        var windowHeight = window.innerHeight || document.documentElement.clientHeight;

        // Если фотография видима на экране, применить вращение
        if (rect.top >= 0 && rect.bottom <= windowHeight) {
            rotateImage(image);
        }
    }
}

// Добавить обработчик события скроллинга страницы
window.addEventListener('scroll', handleScroll);