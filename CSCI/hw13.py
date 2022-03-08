import turtle, math, random
'''
Make it so that the left and right walls loop (that is, going off the left edge of the window teleports the ship to the right edge, and vice versa).
Move all of the messages into the turtle window so that we don’t have to look at terminal
'''
class SpaceCraft(turtle.Turtle):
    '''
    Purpose: An object of this class represents a spacecraft. This spacecraft inherits from a turtle.
    Instance variables:
        vx: a float representing the horizontal velocity of the spacecraft.
        vy: a float representing the vertical velocity of the spacecraft.
        fuel: an int representing the fuel level of the spacecraft.
    Methods:
        __int__: the constructor to instantiate the spacecraft by  first calling the turtle constructor then instantiating the other instance variables.\
        move: the method to move the spacecraft based on gravity.
        thrust: the method to move the spacecraft based upon the angle of the spacecraft and the velocity of the spacecraft.\
        turnleft: the method to turn the spacecraft to the left.
        turnright: the method to turn the spacecraft to the right.
    '''
    def __init__(self, xpos, ypos, xvel, yvel):
        turtle.Turtle.__init__(self)
        self.vx = xvel
        self.vy = yvel
        self.fuel = 50
        self.left(90)
        self.penup()
        self.speed(0)
        self.setpos(xpos,ypos)
    def move(self):
        self.vy = self.vy-0.0486
        xpos = self.xcor()+self.vx
        ypos = self.ycor()+self.vy
        self.setpos(xpos,ypos)
    def thrust(self):
        print("Up Button Pressed")
        if self.fuel>0:
            self.fuel-=1
            angle = math.radians(self.heading())
            self.vx += math.cos(angle)
            self.vy += math.sin(angle)
            print(self.fuel)
        else:
            print("Out of Fuel")
    def turnleft(self):
        print("Left")
        if self.fuel>0:
            self.fuel-=1
            self.left(15)
            print(self.fuel)
        else:
            print("Out of Fuel")
    def turnright(self):
        print("Right")
        if self.fuel>0:
            self.fuel-=1
            self.right(15)
            print(self.fuel)
        else:
            print("Out of Fuel")

class Game():
    '''
    Purpose: This class is meant to build the game and keep it running until the spacecraft crashes or lands successfully.
    Instance variables:
        oblist: a list of the obstables/meteors.
        player: an instance of the spacecraft class meant to represent the player.
    Methods:
        __int__: the constructor to instantiate the game.
        gameloop: the method meant to start and keep the game running until the player lands successfully or crashes.
    '''
    def __init__(self):
        turtle.setworldcoordinates(0, 0, 1000, 1000)
        turtle.delay(0)
        self.oblist = []
        for i in range(10):
            self.oblist.append(Obstacles())
        self.player = SpaceCraft(random.uniform(100,900),random.uniform(500,900),random.uniform(-5,5),random.uniform(-5,0))
        self.player.turtlesize(2)
        self.gameloop()
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.turnleft, 'Left')
        turtle.onkeypress(self.player.turnright, 'Right')
        turtle.listen()
        turtle.mainloop()
    def gameloop(self):
        self.player.move()
        for i in range(len(self.oblist)):
            self.oblist[i].obmove()
            if abs(self.oblist[i].xcor()-self.player.xcor())<25 and abs(self.oblist[i].ycor()-self.player.ycor())<25:
                turtle.setpos(500,100)
                turtle.write("You Crashed!",False, "center",font=("Arial", 20, "normal"))
                return "Done"
        if self.player.xcor()>1000:
            ypos = self.player.ycor()
            self.player.setpos(0,ypos)
        if self.player.xcor()<0:
            ypos = self.player.ycor()
            self.player.setpos(1000,ypos)
        if self.player.ycor()<10:
            print("Done")
            if self.player.vx > -4 and self.player.vx < 4 and self.player.vy > -4 and self.player.vy < 4:
                turtle.penup()
                turtle.setpos(500,100)
                turtle.write("Successful Landing",False, "center",font=("Arial", 20, "normal"))
                return "Done"
                exit()
            else:
                turtle.penup()
                turtle.setpos(500,100)
                turtle.write("You Crashed!",False, "center",font=("Arial", 20, "normal"))
        else:
            turtle.ontimer(self.gameloop, 30)

class Obstacles(turtle.Turtle):
    '''
    Purpose: An object of this class represents an obstacle/meteor.
    Instance variables:
        vx: a float representing the horizontal velocity of the spacecraft.
        vy: a float representing the vertical velocity of the spacecraft.
    Methods:
        __int__: the constructor to instantiate the obstacle and its velocity.
        move: the method to move the obstacles based on gravity.
    '''
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.vx = random.uniform(-5,5)
        self.vy = random.uniform(-5,0)
        self.penup()
        self.speed(0)
        self.setpos(random.uniform(0,1000), 1000)
        self.color("blue")
        self.shape("circle")
        self.turtlesize(2)
    def obmove(self):
        self.vy = self.vy - 0.0486
        xpos = self.xcor() + self.vx
        ypos = self.ycor() + self.vy
        self.setpos(xpos,ypos)
        if self.xcor() < 0 or self.xcor()>1000 or self.ycor()<0 :
            self.setpos(random.uniform(0,1000),1000)



Game()
