from robot import Robot

class Fleet:
    def __init__ (self):
        self.robots = []

    
    def create_fleet (self):
        robot1 = Robot("R2D2")
        self.robots.append(robot1)
        robot2 = Robot("c3po")
        self.robots.append(robot2)
        robot3 = Robot("BB3")
        self.robots.append(robot3)

  






