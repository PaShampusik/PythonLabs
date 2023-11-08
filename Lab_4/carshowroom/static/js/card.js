var card = document.querySelector('.card');
var cardInner = document.querySelector('.card-inner');

card.addEventListener('mousemove', function (event) {
    var rect = card.getBoundingClientRect();
    var mouseX = event.clientX - rect.left;
    var mouseY = event.clientY - rect.top;
    var rotateY = (mouseX / rect.width - 0.5) * 40;
    var rotateX = (0.5 - mouseY / rect.height) * 40;
    cardInner.style.transform = 'rotateY(' + rotateY + 'deg) rotateX(' + rotateX + 'deg)';
});

card.addEventListener('mouseleave', function () {
    cardInner.style.transform = 'none';
});