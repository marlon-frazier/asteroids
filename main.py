import turtle
from turtle import Turtle

#set up screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Asteroid Blaster! by Marlon Frazier')


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('triangle')
        self.shapesize(stretch_len=1.5)
        self.color('red')

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass

player = Player()









screen.exitonclick()