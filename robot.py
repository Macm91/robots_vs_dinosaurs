from weapon import Weapon 

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Saw")
        self.attack = ""

    
    def attack(self): 
        self.attack = Weapon.attack_power
        


