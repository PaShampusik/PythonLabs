var employees = [
    {
        "фамилия": "Иванов",
        "имя": "Иван",
        "отчество": "Иванович",
        "пол": "мужской",
        "стаж": 5
    },
    {
        "фамилия": "Петрова",
        "имя": "Мария",
        "отчество": "Александровна",
        "пол": "женский",
        "стаж": 3
    },
    {
        "фамилия": "Сидоров",
        "имя": "Алексей",
        "отчество": "Петрович",
        "пол": "мужской",
        "стаж": 8
    },
    {
        "фамилия": "Смирнова",
        "имя": "Екатерина",
        "отчество": "Андреевна",
        "пол": "женский",
        "стаж": 2
    },
    // ... дополнительные записи о сотрудниках
];

// Вывод ассоциативного массива на странице
var arrayOutput = document.getElementById("arrayOutput");
arrayOutput.textContent = JSON.stringify(employees, null, 2);

// Функция для добавления новых элементов в ассоциативный массив
function addEmployee() {
    var surname = document.getElementById("surname").value;
    var name = document.getElementById("name").value;
    var patronymic = document.getElementById("patronymic").value;
    var gender = document.getElementById("gender").value;
    var experience = document.getElementById("experience").value;

    var newEmployee = {
        "фамилия": surname,
        "имя": name,
        "отчество": patronymic,
        "пол": gender,
        "стаж": Number(experience)
    };

    employees.push(newEmployee);

    // Очистка полей формы
    //document.getElementById("surname").value = "";
    //document.getElementById("name").value = "";
    //document.getElementById("patronymic").value = "";
    //document.getElementById("gender").value = "";
    //document.getElementById("experience").value = "";

    // Обновление вывода ассоциативного массива на странице
    arrayOutput.textContent = JSON.stringify(employees, null, 2);

    // Вызов функции для обновления списка самых частых имен
    updateMostCommonNames();
}

function getMostCommonNames(employees, gender, count) {
    var nameCounts = {};

    employees.forEach(function (employee) {
        if (employee["пол"] === gender) {
            var name = employee["имя"];
            if (nameCounts[name]) {
                nameCounts[name]++;
            } else {
                nameCounts[name] = 1;
            }
        }
    });

    var nameArray = Object.entries(nameCounts);

    nameArray.sort(function (a, b) {
        return b[1] - a[1];
    });

    var mostCommonNames = nameArray.slice(0, count);

    var resultHtml = '<ul>';
    mostCommonNames.forEach(function (name) {
        resultHtml += '<li>' + name[0] + ': ' + name[1] + '</li>';
    });
    resultHtml += '</ul>';

    document.getElementById('result').innerHTML = resultHtml;
}

function updateMostCommonNames() {
    var gender = document.getElementById("g").selectedIndex;

    if (gender == 0) {
        getMostCommonNames(employees, "мужской", 1);
    } else if (gender == 1) {
        getMostCommonNames(employees, "женский", 1);
    }
}

var genderSelect = document.getElementById("g");

updateMostCommonNames();