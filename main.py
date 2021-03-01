from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

myscreen = Screen()
myscreen.tracer(0)
myscreen.setup(width=600, height=600)

myplayer = Player()
myscreen.listen()
myscreen.onkey(myplayer.move, "Up")

car = CarManager()
scoreboard = Scoreboard()

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    car.move()
    counter += 1
    myscreen.update()
    if myplayer.ycor() > 280:
        myplayer.start()
        scoreboard.point()
        car.level_up()

    if counter % 6 == 0:
        car.create_cars()
        counter = 0

    for i in car.allcars:
        if i.distance(myplayer) < 20:
            game_is_on = False
            scoreboard.game_over()








myscreen.exitonclick()