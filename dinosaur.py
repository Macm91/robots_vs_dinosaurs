class Dino:
    def __init__ (self, name):
        self.name = name
        self.health = 100
        self.attack_power = 0
        self.attack = ""
    
    def dino_attack(self):
        self.attack = input ("Enter 1 to bite or 2 to hit with your tail.")
            if (self.attack == "bite"):
                self.attck_power = 10
            elif (self.attack == "tail"):
                self.attack_power = 15

