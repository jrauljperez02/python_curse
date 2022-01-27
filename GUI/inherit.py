class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Inhale, exhale')

    def get_eyes(self):
        return self.num_eyes
        
class Human:
    pass


class Fish(Animal,Human):
    def __init__(self):
        super().__init__()
        self.color = 'golden'

    def breathe(self):
        super().breathe()
        print('Doing this under water')

        
dog = Animal()
dog.breathe()

print('-----------------------------------')


fish = Fish()
fish.breathe()