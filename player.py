from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVING_DISTANCE = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.initialise()
        self.seth(90)

    def initialise(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVING_DISTANCE)