from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.speed(0)
        self.goto(-200, 280)

    def display_level(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=("Courier", 12, "normal"))

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
