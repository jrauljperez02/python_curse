#Waiter
class Waiter:
    def __init__(self,name,age,weekemd):
        #attributes
        self.name = name
        self.age = age
        self.gender = 'male'
        self.work_on_weekends = weekemd

        self.introduce()
        self.menu()

    def introduce(self):
        print(f'Hello, my name is {self.name}')

    def menu(self):
        print('The menu today is...')

    def work_on_weekend(self):
        if self.work_on_weekends:
            print(f'{self.name} works on weekends')
        else:
            print(f'{self.name} does not work on weekends')

    
waiter1 = Waiter('raul',20,False)
waiter1.work_on_weekend()


#waiter2 = Waiter('antonio',24,False)

