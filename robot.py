from weapon import Weapon 

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Saw", 35)
        self.attack = ""

    
    def attack(self): 
        self #will be void

