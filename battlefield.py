from robot import Robot
from dinosaur import Dino
from herd import Herd
from fleet import Fleet

class battlefield:
    def __init__(self): #Not a declaration but a constructor
        self.fleet = Fleet().create_fleet()
        self.herd = Herd()
        self.game = ""
        self.welcome = ""
        self.dino_turn= ""

    def run_game(self, run):
        self.game = run        

    def display_welcome(self):
        self.welcome = "Begin Game!"
        print (self.welcome)

    def battle(self):
         while (Fleet.health > 0  and  Herd.health > 0 ):
             for i in range(len(Fleet.robots)):
                 Robot.attack
                 
            for i in range(len(Herd.dinosaurs)):
                 Dino.dino_attack

                  
    def dino_turn (self, dinosaur):
        
        self.dino_turn=  Dino.dino_attack

        #something like robot health= robot health - Dino.attack_power
        
    def robo_turn(self, robot):

    #dino health = dino health - robot attack power

    def show_dino_opponent_options(self):
        self.


    def show_robo_opponents_options(self):

    
    def display_winners (self):



        #cycle through dinos to robo 
        #battle round pass in the index. While health >0, keep playing 
        #pass in index. it'll say of fleet robot.index attack dino.index. 
