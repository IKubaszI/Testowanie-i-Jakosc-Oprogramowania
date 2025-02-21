def max(digits):
    if not digits:
        return None

    if digits is None:
        return None

    Hight = digits[0]

    for i in digits:
        if i > Hight:
            Hight = i
    return Hight

def perfectNum(digit):
    sum = 0

    for i in range (1 , digit):
        if digit % i == 0:
            sum = sum + i
    if sum == digit:
        print("liczba doskonała")
        return True
    else:
        print("liczba nie doskonała")
        return True
