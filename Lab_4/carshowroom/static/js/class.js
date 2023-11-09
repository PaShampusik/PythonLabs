// Базовый класс "Автомобиль"
function Car(make, model, year, price) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.price = price;
}

// Методы базового класса
Car.prototype.getMake = function () {
    return this.make;
};

Car.prototype.getModel = function () {
    return this.model;
};

Car.prototype.getYear = function () {
    return this.year;
};

Car.prototype.getPrice = function () {
    return this.price;
};

Car.prototype.setPrice = function (newPrice) {
    this.price = newPrice;
};

// Класс-наследник "Новый автомобиль"
function NewCar(make, model, year, price, warranty) {
    Car.call(this, make, model, year, price);
    this.warranty = warranty;
}

// Наследование прототипа с использованием __proto__
NewCar.prototype.__proto__ = Car.prototype;

// Переопределение метода базового класса
NewCar.__proto__.getYear = function () {
    var currentYear = new Date().getFullYear();
    return currentYear - this.year + 1;
};

// Декоратор для метода базового класса
function withDiscount(car) {
    var originalGetPrice = car.getPrice;

    car.getPrice = function () {
        var price = originalGetPrice.call(car);
        return price * 0.9; // 10% скидка
    };

    return car;
}

// Создание экземпляров и вывод результата на страницу
var car1 = new Car("Toyota", "Camry", 2020, 25000);
var car2 = new NewCar("Honda", "Accord", 2021, 30000, 3);
var car3 = new NewCar("Nissan", "Altima", 2022, 35000, 5);

car3 = withDiscount(car3);

var outputElement = document.getElementById("output");
outputElement.innerHTML += "<p>Марка автомобиля: " + car1.getMake() + "</p>";
outputElement.innerHTML += "<p>Модель автомобиля: " + car1.getModel() + "</p>";
outputElement.innerHTML += "<p>Год автомобиля: " + car1.getYear() + "</p>";
outputElement.innerHTML += "<p>Цена автомобиля: " + car1.getPrice() + "</p>";

outputElement.innerHTML += "<p>Марка нового автомобиля: " + car2.getMake() + "</p>";
outputElement.innerHTML += "<p>Модель нового автомобиля: " + car2.getModel() + "</p>";
outputElement.innerHTML += "<p>Год нового автомобиля: " + car2.getYear() + "</p>";
outputElement.innerHTML += "<p>Цена нового автомобиля: " + car2.getPrice() + "</p>";

outputElement.innerHTML += "<p>Марка нового автомобиля со скидкой: " + car3.getMake() + "</p>";
outputElement.innerHTML += "<p>Модель нового автомобиля со скидкой: " + car3.getModel() + "</p>";
outputElement.innerHTML += "<p>Год нового автомобиля со скидкой: " + car3.getYear() + "</p>";
outputElement.innerHTML += "<p>Цена нового автомобиля со скидкой: " + car3.getPrice() + "</p>";