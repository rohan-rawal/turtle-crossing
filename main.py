from turtle import Screen
from player import Player, FINISH_LINE
from car import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car = Car()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1
    car.move_cars()
    score.display_level()

    #Create new cars
    if count % 20 == 0:
        car.create_cars()

    #Detect collision with a car
    for vehicle in car.cars:
        if player.distance(vehicle) < 20:
            game_is_on = False
            score.game_over()

    #Detect finish line
    if player.ycor() == FINISH_LINE:
        score.increase_level()
        player.initialise()
        car.increase_speed()


screen.exitonclick()
