class RulesOfGame:

    """
        Metoda zwraca true, tylko gdy przejscie z polozenia source na destination w jednym ruchu jest zgodne
        z zasadami gry w szachy.
    """
    def is_correct_move(self, source, destination):
        raise NotImplementedError("Subclasses must implement this method")

class Bishop(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return abs(source_col - dest_col) == abs(source_row - dest_row) and source != destination

class Knight(RulesOfGame):
    def is_correct_move(self, source, destination):
        # TODO: Prosze dokonczyc implementacje

        return True
class Rook(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        return abs(source_col == dest_col) == abs(source_row - dest_row) and source != destination or abs(source_col == dest_col) - abs(source_row == dest_row) and source != destination

class King(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        return abs(source_col - dest_col) == 1 or abs(source_row - dest_row) == 1 and source != destination
class Queen(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        return abs(source_col - dest_col) == abs(source_row - dest_row) and source != destination


# TODO: Prosze dokonczyc implementacje kolejnych figur szachowych: Knight, King, Queen, Rook, Pawn
# TODO: Klasy powinny dziedziczyc RulesOfGame