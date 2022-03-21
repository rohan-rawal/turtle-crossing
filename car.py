from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.seth(180)
        self.penup()
        self.resizemode("user")
        self.turtlesize(stretch_len=2,stretch_wid=1)
        self.shape("square")
        self.create_cars()

    def create_cars(self):
        self.color(random.choice(COLORS))
        self.goto(random.randint(260, 300), random.randint(-280, 280))
            