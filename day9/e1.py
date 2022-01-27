import os
import time
from logo import *

def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y


def calculator():
    operations_dict = {'+':add,
                       '-':substract,
                       '*':multiply,
                       '/':divide}
    print(logo2)

    x = int(input('Type a number: '))

    for key in operations_dict:
        print(key)

    run_again = True
    while run_again:
        
        
        symbol = input('Select an operation from the dictionary: ')
        y = int(input('Type another number: '))

        calculation_function = operations_dict[symbol]
        result = calculation_function(x,y)

        print(f'{x} {symbol} {y} = {result}')

        print(f'Type "yes" to continue calculating with {result}')
        print('Type "no to run again all the program"')
        repeat = input("Type 'exit' to exit: ")

        if repeat == 'yes'.lower():
            x = result

        elif repeat == 'no'.lower():
            run_again = False
            os.system('clear')
            calculator()

        elif repeat == 'exit'.lower():
            run_again = False

calculator()

    

    


