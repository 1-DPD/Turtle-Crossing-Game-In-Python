from turtle import Turtle
DISTANCE_POSITIVE = 20
DISTANCE_NEGATIVE = -20
FINISH_LINE = 240
class Turtlegame(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("yellow")
        self.setheading(90)
        self.penup()
        self.goto(0, -250)

    def up(self):
        self.setheading(90)
        self.forward(DISTANCE_POSITIVE)


    def down(self):
        self.setheading(90)
        self.forward(DISTANCE_NEGATIVE)

    def finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else :
            return False

    def start_again(self):
        self.goto(0,-250)

    def game_over(self):
        game_over = Turtlegame()
        game_over.color("black")
        game_over.goto(0, 0)
        game_over.write("Game Over...", align="center", font=("Ariel", 30, "normal"))

