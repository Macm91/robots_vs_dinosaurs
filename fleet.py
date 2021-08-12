from robot import Robot

class Fleet:
    def __init__ (self):
        self.robots = []
        self.health = 0
    
    def create_fleet (self):
        robot1 = Robot("R2D2")
        self.robots.append(robot1)
        robot2 = Robot("c3po")
        self.robots.append(robot2)
        robot3 = Robot("BB3")
        self.robots.append(robot3)
        self.health = (robot1.health + robot2.health + robot3.health)
        
        

  






