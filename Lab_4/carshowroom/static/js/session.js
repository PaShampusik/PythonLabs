var countdownElement = document.getElementById('countdown');
var countdownValue = localStorage.getItem('countdown');

if (countdownValue) {
    // Если значение обратного отсчета уже сохранено в локальном хранилище,
    // восстанавливаем его
    countdownValue = parseInt(countdownValue, 10);
} else {
    // Если значение обратного отсчета не сохранено, устанавливаем его на 1 час
    countdownValue = 60 * 60; // 1 час в секундах
    localStorage.setItem('countdown', countdownValue);
}

// Запускаем обратный отсчет
var countdownInterval = setInterval(function () {
    countdownValue--;

    if (countdownValue <= 0) {
        // Обратный отсчет завершен
        clearInterval(countdownInterval);
        countdownElement.textContent = 'Отсчет завершен';
    } else {
        // Обновляем значение обратного отсчета и сохраняем его в локальном хранилище
        countdownElement.textContent = formatTime(countdownValue);
        localStorage.setItem('countdown', countdownValue);
    }
}, 1000);

// Функция для форматирования времени в формате ЧЧ:ММ:СС
function formatTime(seconds) {
    var hours = Math.floor(seconds / 3600);
    var minutes = Math.floor((seconds % 3600) / 60);
    var remainingSeconds = seconds % 60;

    return (
        padZero(hours) +
        ':' +
        padZero(minutes) +
        ':' +
        padZero(remainingSeconds)
    );
}

// Функция для добавления ведущего нуля, если число меньше 10
function padZero(number) {
    return number < 10 ? '0' + number : number;
}

window.addEventListener('beforeunload', function (event) {
    // Проверяем, есть ли значение обратного отсчета в локальном хранилище
    var countdownValue = localStorage.getItem('countdown');

    if (countdownValue && parseInt(countdownValue, 10) <= 0) {
        // Если обратный отсчет завершен, выводим предупреждение
        event.preventDefault(); // Отменяем закрытие окна/вкладки
        event.returnValue = ''; // Задаем пустое значение для сообщения

        // Отображаем предупреждающий диалог
        var confirmationMessage = 'Сессия окончена. Вы уверены, что хотите покинуть страницу?';
        event.returnValue = confirmationMessage; // Для старых версий Firefox

        return confirmationMessage;
    }
});