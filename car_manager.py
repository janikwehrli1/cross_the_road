from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "blue", "green", "purple"]


class CarManager(Turtle):
    def __init__(self):
        self.allcars = []
        self.carspeed = 10


    def create_cars(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.turtlesize(stretch_wid=1, stretch_len=2)
        rand1 = random.randint(-250, 270)
        new_car.goto(x=280, y=rand1)
        self.allcars.append(new_car)

    def move(self):
        for i in self.allcars:
            i.backward(self.carspeed)

    def level_up(self):
        self.carspeed += 5
