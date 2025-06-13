class TimeOfTransfer:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def copy(self):
        return TimeOfTransfer(self.hour, self.minute)

class Transfer:
    def __init__(self, amount, transfer_time):
        self._amount = amount
        self._transfer_time = transfer_time

    def get_transfer_time(self):
        # Problem rozwiązany!
        return self._transfer_time.copy()

    def get_amount(self):
        return self._amount

    def execute_transfer(self):
        print(f"Wykonuje przelew na kwote {self._amount} o godzinie {self._transfer_time}")

scheduled_time = TimeOfTransfer(14, 30)
my_transfer = Transfer(100.00, scheduled_time)

print(f"Poczatkowy czas przelewu: {my_transfer.get_transfer_time()}")
my_transfer.execute_transfer()

# Ups! KtoĹ dobraĹ siÄ do czasu przelewu...
time_from_getter = my_transfer.get_transfer_time()
time_from_getter.hour = 16
time_from_getter.minute = 0

print(f"\nCzas przelewu PO ZEWNETRZNEJ INGERENCJI: {my_transfer.get_transfer_time()}")
my_transfer.execute_transfer()

print("\nUps! Kluczowy czas obiektu przelewu zostal zmanipulowany z zewnatrz. ")
print("Ot tak, integralnosc obiektu zostaĹa naruszona, a to byly czyjes ciezko zarobione pieniadze. ")
print("To tylko zwykly getter(), a jak wiele moze zepsuc")