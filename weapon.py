class weapon:
    #========constructor=======
    def __init__(self):
        self.name = ""
        self.attack_power = 0
#METHODS
    def weapon_details(self, name, power):
        self.name = name
        self.attack_power = power
        print("You have selected the " + name + " as your weapon. It has an attck power of " + str(power))

