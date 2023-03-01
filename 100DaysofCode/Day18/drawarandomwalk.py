import random
import turtle as t

tim=t.Turtle()

colors=["blue", "cyan", "green", "black", "magenta", "red", "yellow"]
directions=[0,90,180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen=t.Screen()
screen.exitonclick()