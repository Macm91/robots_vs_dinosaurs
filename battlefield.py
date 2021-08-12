from robot import Robot
from dinosaur import Dino
from herd import Herd
from fleet import Fleet

class battlefield:
    def __init__(self): #Not a declaration but a constructor
        self.fleet = Fleet().create_fleet()
        self.herd = Herd()
        
    
    def run_game(self):
        pass


    def display_welcome(self):
        pass


    def battle(self):
        pass    
    
#As a developer, I want a Robot to have the ability to attack a Dinosaur 
# Dinosaur to have the ability to attack a Robot on a Battlefield.

    def dino_turn (self, dino):
        self.dino_turn= dino
        #need to fix these

        #cycle through dinos to robo 
        #battle round pass in the index. While health >0, keep playing 
        #pass in index. it'll say of fleet robot.index attack dino.index. 
