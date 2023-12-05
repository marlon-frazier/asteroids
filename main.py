import turtle
from turtle import Turtle
import random

#set up screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Asteroid Blaster! by Marlon Frazier')


class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('triangle')
        self.shapesize(stretch_len=1.5)
        self.color('red')
        self.direction = 0

    def rotate_left(self):
        self.left(20)
        self.direction = self.heading()
        print(self.heading())

    def rotate_right(self):
        self.right(20)
        self.direction = self.heading()
        print(self.heading())




class Asteroid(Turtle):
    def __init__(self):
        super().__init__()
        direction = random.randint(0, 3)
        self.penup()
        self.speed(0)
        self.color('gray')
        self.shape('circle')
        self.speed = 2
        if direction == 0:
            self.goto(450, random.randint(-450, 450))
        elif direction == 1:
            self.goto(-450, random.randint(-450, 450))
        elif direction == 2:
            self.goto(random.randint(-450, 450), 450)
        elif direction == 3:
            self.goto(random.randint(-450, 450), -450)

    def move(self):
        x,y = self.position()
        if x > 0:
            self.setx(x - self.speed)
        elif x < 0:
            self.setx(x + self.speed)
        if y > 0:
            self.sety(y - self.speed)
        elif y < 0:
            self.sety(y + self.speed)


class Missile(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape('circle')
        self.color('yellow')
        self.shapesize(.5, .5)
        self.speed = 5
        self.state = 'ready'

    def shoot(self, direction):
        if self.state == 'ready':
            self.state = 'fire'
            self.goto(0, 0)
            self.setheading(direction)
            self.showturtle()

    def move(self):
        if self.state == 'fire':
            self.forward(self.speed)
            #check if the missile is out of bounds
            if not (-300 < self.xcor() < 300 and -300 < self.ycor() < 300):
                self.hideturtle()
                self.state = 'ready'



spaceship = Spaceship()
asteroid = Asteroid()
missile = Missile()

#Set keyboard bindings
turtle.listen()
turtle.onkey(spaceship.rotate_left, "Left")
turtle.onkey(spaceship.rotate_right, "Right")
turtle.onkey(lambda: missile.shoot(spaceship.direction) , "space")
game_is_on = True

while game_is_on:
    asteroid.move()
    missile.move()
    turtle.update()






screen.exitonclick()