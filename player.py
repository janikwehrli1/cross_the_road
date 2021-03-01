from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(0, -280)

    def move(self):
        self.forward(20)

    def start(self):
        self.goto(0, -280)