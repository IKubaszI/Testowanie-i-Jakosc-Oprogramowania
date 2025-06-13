class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age < 0:
            print(f"Wiek nie może być ujemny!")
            return

        if new_age >110:
            print(f"Wiek jest zbyt duży!")
            return

        else:
            self._age = new_age

user = User("Jan", 30)
print(f"Poczatkowy wiek: {user.get_age()}")

user.set_age(-5)
print(f"Wiek po ustawieniu nieprawidlowej wartosci: {user.get_age()}")

user.set_age(200)
print(f"Wiek po ustawieniu absurdalnie duzej wartosci: {user.get_age()}")

user.set_age(34)
print(f"Wiek po ustawieniu normalnej wartosci: {user.get_age()}")
