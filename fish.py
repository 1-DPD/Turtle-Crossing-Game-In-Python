from turtle import Turtle
import random
COLORS = ["red", "pink", "yellow", "blue", "orange"]
DISTANCE = 5
class Fish(Turtle):
    def __init__(self):
        super().__init__()
        self.fishes = []
        self.speed = DISTANCE

        self.hideturtle()

    def create_fish(self):
        random_no = random.randint(1, 6)
        if random_no == 1:
            new_fish = Turtle()
            new_fish.shape("square")
            new_fish.color(random.choice(COLORS))
            new_fish.penup()
            new_fish.shapesize(stretch_wid=1, stretch_len=4)
            y_cor = random.randint(-200, 200)
            new_fish.goto(260, y_cor)
            self.fishes.append(new_fish)


    def move(self):
        for fish in self.fishes:
            fish.backward(self.speed)

    def fish_speed(self):
        self.speed += DISTANCE

