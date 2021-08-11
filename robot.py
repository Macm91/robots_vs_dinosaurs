class robot:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.weapon = []
        self.attack = ""

    def robot_details(self, name, weapon):
        self.name = name
        self.health = 100
        self.weapon = weapon
        print(self.name, self.health, self.weapon)
    
    def attack(self): 
        self #will be void