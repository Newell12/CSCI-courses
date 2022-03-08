import turtle, random
count = 0
'''
I changed this function by adding in another paddle and creating a count variable that counts the amount of times a ball has hit the paddle.
'''
class BouncingBall(turtle.Turtle):
    def __init__(self, posx, posy, color, velx, vely, paddle, paddle2):
        turtle.Turtle.__init__(self)
        self.vx = velx
        self.vy = vely
        self.penup()
        self.speed(0)
        self.setpos(posx, posy)
        self.color(color)
        self.shape('circle')
        self.paddle = paddle
        self.paddle2 = paddle2
        self.animate()
    def animate(self):
        global count
        xcur = self.xcor()
        ycur = self.ycor()
        self.vy -= 0.6
        xcur += self.vx
        ycur += self.vy
        px = self.paddle.xcor()
        px2 = self.paddle2.xcor()
        missed = False
        if xcur < 0:
            xcur = 0
            self.vx *= -1
        if xcur > 400:
            xcur = 400
            self.vx *= -1
        if ycur < 0:
            missed = True
            self.hideturtle()
            #ycur = 0
            #self.vy *= -1
        if ycur > 400:
            ycur = 400
            self.vy *= -1
        if 10 < ycur < 50 and px-30 < xcur < px + 30:
            ycur = 50
            self.vy *= -1
            count = count + 1
            print(count)
        if 10 < ycur < 50 and px2-30 < xcur < px2 + 30:
            ycur = 50
            self.vy *= -1
            count = count + 1
            print(count)
        self.setpos(xcur, ycur)
        if missed == False:
            turtle.ontimer(self.animate, 30)
turtle.setworldcoordinates(0, 0, 400, 400)
turtle.delay(0)
paddle = turtle.Turtle()
paddle2 = turtle.Turtle()
paddle.penup()
paddle.speed(0)
paddle.shape('square')
paddle.shapesize(0.5, 4)
paddle.setpos(300, 30)
paddle2.penup()
paddle2.speed(0)
paddle2.shape('square')
paddle2.shapesize(0.5, 4)
paddle2.setpos(100, 30)
def move_left():
    px = paddle.xcor()
    py = paddle.ycor()
    px = px - 20
    paddle.setpos(px, py)
    px2 = paddle2.xcor()
    py2 = paddle2.ycor()
    px2 = px2 - 20
    paddle2.setpos(px2, py2)
def move_right():
    px = paddle.xcor()
    py = paddle.ycor()
    px = px + 20
    paddle.setpos(px, py)
    px2 = paddle2.xcor()
    py2 = paddle2.ycor()
    px2 = px2 + 20
    paddle2.setpos(px2, py2)
turtle.onkeypress(move_left, 'Left')
turtle.onkeypress(move_right, 'Right')
for i in range(10):
    xpos = random.uniform(0, 400)
    ypos = random.uniform(200, 400)
    xvel = random.uniform(-4, 4)
    yvel = random.uniform(-4, 4)
    color = random.choice(['red', 'green', 'blue', 'purple'])
    b = BouncingBall(xpos, ypos, color, xvel, yvel, paddle, paddle2)
turtle.listen()
turtle.mainloop()
