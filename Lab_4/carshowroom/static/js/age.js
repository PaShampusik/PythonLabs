function checkAge() {
    var dobInput = document.getElementById("dob");
    var dob = new Date(dobInput.value);

    // Проверка валидности введенной даты
    if (isNaN(dob.getTime())) {
        alert("Пожалуйста, введите корректную дату рождения.");
        return;
    }

    var currentDate = new Date();
    var age = currentDate.getFullYear() - dob.getFullYear();

    // Проверка, является ли дата рождения в будущем
    if (dob > currentDate) {
        alert("Пожалуйста, введите дату рождения из прошлого или сегодняшнюю дату.");
        return;
    }

    // Проверка, является ли пользователь совершеннолетним (18 лет и старше)
    if (age >= 18) {
        var dayOfWeek = dob.toLocaleDateString("en-US", { weekday: "long" });
        document.getElementById("result").innerHTML = "Вы совершеннолетний. День недели вашего рождения: " + dayOfWeek;
    } else {
        alert("Для использования сайта требуется разрешение родителей.");
    }
}