from dinosaur import Dino

class Herd:
    def __init__ (self):
        self.dinosaurs = []
        dino1 = Dino("Little Foot")
        self.dinosaurs.append(dino1)
        dino2 =Dino("Bobbie Flay")
        self.dinosaurs.append(dino2)
        dino3 = Dino("Diplodercus")
        self.dinosaurs.append(dino3)
        self.health = (dino1.health + dino2.health + dino3.health)
        