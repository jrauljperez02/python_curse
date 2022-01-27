from coffee_maker import CoffeeMaker
from menu import *


"""Let's create all the objects we'll use"""
coffee_maker = CoffeeMaker()
menu = Menu()



#coffee_maker.report()
print(menu.get_items())


print(menu.find_drink('espresso'))

