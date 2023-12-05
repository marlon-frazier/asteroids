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
        self.left(20)

    def rotate_right(self):
        self.right(20)

player = Player()

#Set keyboard bindings
turtle.listen()
turtle.onkey(player.rotate_left, "Left")
turtle.onkey(player.rotate_right, "Right")

turtle.mainloop()







screen.exitonclick()