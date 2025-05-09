class PeselValidator:
    def __init__(self, pesel: str):
        self.pesel = pesel

    def is_valid(self) -> bool:
        if not self.pesel or not self.pesel.isdigit() or len(self.pesel) != 11:
            return False

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        checksum = sum(int(d) * w for d, w in zip(self.pesel[:10], weights))
        control_digit = (10 - (checksum % 10)) % 10

        return control_digit == int(self.pesel[-1])

    def field_name(self) -> str:
        return "pesel"
