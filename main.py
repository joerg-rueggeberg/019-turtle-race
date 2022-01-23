from random import randint
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
s = Screen()
s.setup(width=500, height=400)
bet = s.textinput(title="Make your bet.", prompt="Which turtle will win the race?\n\n"
                                                 "Enter a color:\n"
                                                 "(red, orange, yellow, green, blue, purple)")
print(f"your bet: {bet}")
height = 200
step = 55

for c in colors:
    t = Turtle(shape="turtle")
    t.pu()
    t.color(c)
    height -= step
    t.goto(x=-225, y=height)
    turtles.append(t)

race_is_on = True
while race_is_on:
    for t in turtles:
        t.forward(randint(0, 5))
        if t.xcor() > 230:
            winner = t.pencolor()
            race_is_on = False
            if winner == bet:
                print(f"you won. {winner} won the race.")
            else:
                print(f"you lost. {winner} won the race.")

s.exitonclick()
