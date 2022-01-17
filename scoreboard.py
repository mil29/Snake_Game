from turtle import Turtle
from snake import Snake
from food import Food

ALIGNMENT = "center"
FONT = ("courier", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.color("White")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode='w') as new_high:
            new_high.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



