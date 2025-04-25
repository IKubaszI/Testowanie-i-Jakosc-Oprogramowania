function board() {
    const board = document.createElement('div');
    board.className = 'chessboard effect';

    const letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];

    for (let row = 8; row >= 1; row--) {
        for (let col = 0; col < 8; col++) {
            const field = document.createElement('div');
            field.classList.add('field');

            const isWhite = (row + col) % 2 === 0;
            field.classList.add(isWhite ? 'white' : 'black');

            const id = `${letters[col]}_${row}`;
            field.id = id;

            // Dodaj figurę w c_1
            if (id === 'c_1') {
                const span = document.createElement('span');
                span.id = 'figure';
                span.innerHTML = '&#9815;'; // ♝ biskup
                field.appendChild(span);
            }


            board.appendChild(field);
        }
    }

    document.getElementById('board-container').appendChild(board);
}

function isCorrectMove(source, destination, type) {
    const figure = {
        source: source,
        destination: destination,
        figureType: type
    };

    return fetch('/api/chess/is-correct-move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(figure)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Błąd sieci lub serwera');
            }

            return response.json();
        })
        .then(data => {
            if(data === false) {
                alert("Ruch niepoprawny!")
            }

            return data;
        })
        .catch(error => {
            console.error("error...", error);
            alert("Wystąpił nieoczekiwany problem z usługą!");
            return false;
        });
}

document.addEventListener('DOMContentLoaded', () => {
    board();

    let chooseFigure = 'BISHOP';

    const figures = new Map([
        ['KING', '<span id="figure">&#9812;</span>'],
        ['QUEEN', '<span id="figure">&#9813;</span>'],
        ['ROOK', '<span id="figure">&#9814;</span>'],
        ['BISHOP', '<span id="figure">&#9815;</span>'],
        ['KNIGHT', '<span id="figure">&#9816;</span>'],
        ['PAWN', '<span id="figure">&#9817;</span>']
    ]);

    let startPosition = null;
    let destinationPosition = null;

    const select = document.getElementById('chess');
    select.addEventListener('change', (event) => {
        chooseFigure = event.target.value;

        const oldFigure = document.getElementById('figure');
        if (oldFigure) oldFigure.remove();

        let targetFieldId = {
            'KING': 'e_1',
            'QUEEN': 'd_1',
            'ROOK': 'a_1',
            'BISHOP': 'c_1',
            'KNIGHT': 'b_1',
            'PAWN': 'd_2'
        }[chooseFigure];

        const targetField = document.getElementById(targetFieldId);
        if (targetField) targetField.innerHTML = figures.get(chooseFigure);
    });

    document.querySelectorAll('.field').forEach(field => {
        field.addEventListener('mouseup', () => {
            const figureElement = field.querySelector('#figure');
            const fieldId = field.id;

            if (figureElement && startPosition === null) {
                startPosition = fieldId;
                figureElement.style.color = '#267340';
            } else if (startPosition !== null) {
                destinationPosition = fieldId;

                isCorrectMove(startPosition, destinationPosition, chooseFigure)
                    .then(response => {
                        const oldFigure = document.getElementById('figure');
                        if (oldFigure) oldFigure.style.color = '#000000';

                        if (response) {
                            if (oldFigure) oldFigure.remove();
                            const target = document.getElementById(destinationPosition);
                            if (target) target.innerHTML = figures.get(chooseFigure);
                        } else {
                            if (oldFigure) oldFigure.remove();
                            const original = document.getElementById(startPosition);
                            if (original) original.innerHTML = figures.get(chooseFigure);
                        }

                        startPosition = null;
                        destinationPosition = null;
                    });
            }
        });
    });
});
