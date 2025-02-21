from src.math_lib import max
from src.math_lib import perfectNum
print("Testy rozpoczeły się")
print("")
def max_test():

    #Arrange
    tabp = [6,8,4,3,9,1]
    #Act
    result = max(tabp)
    #Assert
    assert result == 9
print("Test max pozytywny")
print("")


def perfectNum_test():

    #Arrange
    number = 8128
    #Act
    result = perfectNum(number)

    #Assert
    assert result == True


    #Test
max_test()
perfectNum_test()

    #Print
print("")
print("Testy zakonczone")


