__author__ = 'Saturn'
def max_of_three(number1, number2, number3):
    if number1 > number2 & number3:
        return number1
    elif number2 > number1 & number3:
        return number2
    elif number3 > number1 & number2:
        return number3
    else:
        print"All these numbers are the same!"
max_of_three(19
