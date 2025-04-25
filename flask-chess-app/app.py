from flask import Flask, request, jsonify, render_template
from services.chess_service import ChessService

import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

chess_service = ChessService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chess/is-correct-move', methods=['POST'])
def is_correct_move():
    move_data = request.get_json()
    logger.info(f"*** move details : {move_data}")

    is_correct = chess_service.is_correct_move(move_data)

    return jsonify(is_correct), 200

if __name__ == '__main__':
    app.run(debug=True)