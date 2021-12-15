import os
import time

def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

operations_dict = {'+':add,
                   '-':substract,
                   '*':multiply,
                   '/':divide}

symbols_list = ['+','-','*','/']

for _ in range(0,3):
    

    symbol = input('Select an operation from the dictionary: ')
    if symbol in symbols_list:

        calculation_function = operations_dict[symbol]

        x = int(input('Type a number: '))
        y = int(input('Type another number: '))

        result = calculation_function(x,y)
        print(result)
    elif symbol not in symbols_list:
        print('Invalid symbol')

    time.sleep(3)
    os.system('clear')

    

    


