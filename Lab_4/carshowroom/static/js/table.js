const tableContainer = document.getElementById('table-container');
const transposeButton = document.getElementById('transpose-button');
const addRowButton = document.getElementById('add-row-button');
const addColumnButton = document.getElementById('add-column-button');
const maxSelectionInput = document.getElementById('max-selection');
const table = document.getElementById('table');

let maxSelection = 1;
let selectedCells = [];

const tableSizeInput = document.getElementById('table-size');
const createTableButton = document.getElementById('create-table-button');

createTableButton.addEventListener('click', () => {
    const newSize = parseInt(tableSizeInput.value);
    if (!isNaN(newSize) && newSize > 0) {
        height = newSize;
        width = newSize;
        generateTable(width, height);
        selectedCells = [];
    }
});


function generateTable(width, height) {
    table.innerHTML = '';

    for (let i = 0; i < height; i++) {
        const row = document.createElement('tr');
        for (let j = 0; j < width; j++) {
            const cell = document.createElement('td');
            cell.textContent = Math.floor(Math.random() * 100); // Случайные числа
            row.appendChild(cell);

            cell.addEventListener('click', () => handleCellClick(cell));
        }
        table.appendChild(row);
    }
}

function handleCellClick(cell) {
    if (!cell.classList.contains('selected')) {
        if (selectedCells.length < maxSelection) {
            if (!findNeigbour(cell, selectedCells)) {
                cell.classList.add('selected');
                selectedCells.push(cell);
            }
        }
    } else {
        cell.classList.remove('selected');
        selectedCells = selectedCells.filter((selectedCell) => selectedCell !== cell);
    }
}

function findNeigbour(new_cell, all) {
    let result = all.reduce(function (acc, item) {
        return acc || areNeighbours(new_cell, item);
    }, false)

    return result;
}

function areNeighbours(cell1, cell2) {
    const row1 = cell1.parentNode;
    const row2 = cell2.parentNode;
    const table = row1.parentNode;
    const columnIndex1 = Array.from(row1.children).indexOf(cell1);
    const columnIndex2 = Array.from(row2.children).indexOf(cell2);
    const rowIndex1 = Array.from(table.children).indexOf(row1);
    const rowIndex2 = Array.from(table.children).indexOf(row2);
    return (Math.abs(rowIndex1 - rowIndex2) + Math.abs(columnIndex1 - columnIndex2)) == 1;
}

transposeButton.addEventListener('click', () => {
    transposeTable();
    selectedCells.forEach((cell) => cell.classList.remove('selected'));
    selectedCells = [];
});

addRowButton.addEventListener('click', () => {
    height++;
    generateTable(width, height);
    selectedCells.forEach((cell) => cell.classList.remove('selected'));
    selectedCells = [];
});

addColumnButton.addEventListener('click', () => {
    width++;
    generateTable(width, height);
    selectedCells.forEach((cell) => cell.classList.remove('selected'));
    selectedCells = [];
});


maxSelectionInput.addEventListener('input', () => {
    maxSelection = parseInt(maxSelectionInput.value);
    selectedCells.forEach((cell) => cell.classList.remove('selected'));
    selectedCells = [];
});

function transposeTable() {
    const rows = Array.from(table.querySelectorAll('tr'));
    const newTable = Array.from({ length: width }, () => []);
    width = [height, height = width][0];

    rows.forEach((row, rowIndex) => {
        row.querySelectorAll('td').forEach((cell, colIndex) => {
            newTable[colIndex][rowIndex] = cell;
        });
    });

    table.innerHTML = '';

    newTable.forEach((newRow) => {
        const row = document.createElement('tr');
        newRow.forEach((cell) => row.appendChild(cell));
        table.appendChild(row);
    });
}