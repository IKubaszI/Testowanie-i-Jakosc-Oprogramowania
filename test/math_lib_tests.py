from src.math_lib import max
from src.math_lib import perfectNum
print("")
print("Testy rozpoczeły się")
print("")
def max_test():

    #Arrange
    tabp = [6,8,4,3,9,1]
    #Act
    result = max(tabp)
    #Assert
    assert result == 9, "test1 winik powinien wynosic 9"

    #Arrange
    tabp = [2,1,3,2,1,5]
    #Act
    result = max(tabp)
    #Assert
    assert result == 5, "test2 winik powinien wynosic 5"

    #Arrange
    tabp = [7,1,3,2,1,5]
    #Act
    result = max(tabp)
    #Assert
    assert result == 7, "test3 winik powinien wynosic 7"

print("Test max pozytywny")
print("")


def perfectNum_test():

    #Arrange
    number = 8128
    #Act
    result = perfectNum(number)

    #Assert
    assert result == True, "test1 powinno zwracac True"

    #Arrange
    number = 2
    #Act
    result = perfectNum(number)

    #Assert
    assert result == True, "test2 powinno zwracac True"


    #Test
max_test()
perfectNum_test()

    #Print

print("Testy zakonczone")
print("")

