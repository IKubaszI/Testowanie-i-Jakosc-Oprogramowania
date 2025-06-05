# src/chess_service.py

import logging
from .rules_of_game import Bishop, Knight, Rook, King, Queen, Pawn

logger = logging.getLogger(__name__)

def _convert_to_point(algebraic_notation):
    sign_fields = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    number_fields = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}

    if not algebraic_notation or len(algebraic_notation) != 3 or algebraic_notation[1] != '_':
        return None

    x_char = algebraic_notation[0].lower()
    y_char = algebraic_notation[2]

    if x_char in sign_fields and y_char in number_fields:
        x = sign_fields[x_char]
        y = number_fields[y_char]
        return x, y
    return None

class ChessService:
    def __init__(self):
        self.bishop_rules = Bishop()
        self.knight_rules = Knight()
        self.rook_rules = Rook()
        self.king_rules = King()
        self.queen_rules = Queen()
        self.pawn_rules = Pawn()

    def is_correct_move(self, move_data):
        source = _convert_to_point(move_data.get('source'))
        destination = _convert_to_point(move_data.get('destination'))
        figure_type = move_data.get('figureType')

        logger.info(f"*** move after convert, source      : {source}")
        logger.info(f"*** move after convert, destination : {destination}")
        logger.info(f"*** figure type                     : {figure_type}")

        if figure_type == 'BISHOP':
            return self.bishop_rules.is_correct_move(source, destination)
        elif figure_type == 'KNIGHT':
            return self.knight_rules.is_correct_move(source, destination)
        elif figure_type == 'ROOK':
            return self.rook_rules.is_correct_move(source, destination)
        elif figure_type == 'KING':
            return self.king_rules.is_correct_move(source, destination)
        elif figure_type == 'QUEEN':
            return self.queen_rules.is_correct_move(source, destination)
        elif figure_type == 'PAWN':
            return self.pawn_rules.is_correct_move(source, destination)
        else:
            return False
