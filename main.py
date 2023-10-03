import time
from turtle import Screen,Turtle
from turtle_game import Turtlegame
from fish import Fish
from score import Score
screen = Screen()

screen.title("Turtle And Fish")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Turtlegame()
fish = Fish()
score = Score()

screen.listen()
screen.onkey(turtle.up, "Up")
screen.onkey(turtle.down, "Down")
screen.onkey(turtle.right, "Right")
screen.onkey(turtle.left, "Left")


game_continue = True
while game_continue:
    time.sleep(0.1)
    screen.update()
    fish.create_fish()
    fish.move()

    for each_fish in fish.fishes:
        if each_fish.distance(turtle) < 25:
            game_continue = False
            turtle.game_over()

    if turtle.finish_line():
        turtle.start_again()
        fish.fish_speed()
        score.level_up()


screen.exitonclick()