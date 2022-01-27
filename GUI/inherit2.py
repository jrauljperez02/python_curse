class Child:
    def __init__(self):
        self.hair_color = 'brown'
        self.is_living_in_house = True
        self.earn_money = True

    def walk(self):
        print("I'm walking")

    def playVideogames(self):
        print('Likes playing videogames')



class Father(Child):
    def __init__(self):
        super().__init__()
        self.age = 45
    
    def walk_to_work(self):
        super().walk()
        print('to the job')

    def playVideogames_at_night(self):
        super().playVideogames()
        print('at night')
    


    