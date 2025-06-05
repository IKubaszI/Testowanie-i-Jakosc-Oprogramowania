# src/rules_of_game.py

class RulesOfGame:
    """
    Metoda zwraca True tylko wtedy, gdy przejście z pola source na pole destination
    w jednym ruchu jest zgodne z zasadami dla danej figury.
    """
    def is_correct_move(self, source, destination):
        raise NotImplementedError("Subclasses must implement this method")


class Bishop(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        # Goniec porusza się po przekątnej: różnica kolumn = różnica wierszy
        return abs(source_col - dest_col) == abs(source_row - dest_row) and source != destination


class Knight(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        dx = abs(source_col - dest_col)
        dy = abs(source_row - dest_row)
        # Skoczek porusza się w kształcie litery „L”: 2 w jedną stronę i 1 w drugą
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


class Rook(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        # Wieża porusza się pionowo lub poziomo: kolumna ta sama i wiersz inny, lub wiersz ten sam i kolumna inna
        return ((source_col == dest_col and source_row != dest_row) or
                (source_row == dest_row and source_col != dest_col)) and source != destination


class King(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        dx = abs(source_col - dest_col)
        dy = abs(source_row - dest_row)
        # Król porusza się o jedno pole w dowolnym kierunku
        return max(dx, dy) == 1 and source != destination


class Queen(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        dx = abs(source_col - dest_col)
        dy = abs(source_row - dest_row)
        # Królowa łączy ruchy wieży i gońca
        diagonal = dx == dy and source != destination
        vertical = (source_col == dest_col and source_row != dest_row)
        horizontal = (source_row == dest_row and source_col != dest_col)
        return diagonal or vertical or horizontal


class Pawn(RulesOfGame):
    def is_correct_move(self, source, destination):
        """
        Zakładamy biały pionek poruszający się "w górę" (rosnące numery wierszy).
        Na pierwszym ruchu (source_row == 2) może iść o 2 pola do przodu (destination_row == 4)
        lub o 1 pole (destination_row == 3). Potem tylko o 1 (destination_row == source_row + 1).
        Zawsze w tej samej kolumnie.
        """
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        if source_col != dest_col:
            return False
        # ruch o jedno pole do przodu
        if dest_row == source_row + 1:
            return True
        # pierwszy ruch: z wiersza 2 na 4
        if source_row == 2 and dest_row == 4:
            return True
        return False
