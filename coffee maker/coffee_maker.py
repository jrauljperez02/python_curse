class CoffeeMaker:
    '''Models the machine that makes coffee'''
    def __init__(self):
        self.resources = {'water':300,
                          'milk':200,
                          'coffee':400}

        '''self.water = 300
        self.milk = 200
        self.coffee = 400'''
    
    def report(self):
        '''Prints a report of all resources'''
        print(f'Water: {self.resources["water"]}ml')
        print(f'Milk:  {self.resources["milk"]}ml')
        print(f'Coffee: {self.resources["coffee"]}g')


    def is_resources_sufficient(self,drink):
        '''Returns True when order can be made, False if indgredients are insufficient'''
        can_make = True
        


