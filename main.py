from turtle import Screen
from player import Player
from car import Car
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player = Player()
for _ in range(10):
    car = Car()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
