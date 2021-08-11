class dino:
    def __init__ (self):
        self.name = ""
        self.health = 100
        self.attack_power = 50
        self.attack = ""

    def dino_details(self, name):
        self.name = name 
        self.attack_power = 50 
        self.health = 100
    
    def dino_attack(self):
        self