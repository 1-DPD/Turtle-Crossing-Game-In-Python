from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=("Ariel", 30, "normal"))

    def level_up(self):
        self.level += 1
        self.update_score()

