from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "orange", "pink", "yellow"]
turtles = []
y_positions = [-70, -40, -10, 20, 50, 80]
screen = Screen()
screen.setup(width=500, height=450)

for n in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[n])
    turtles.append(new_turtle)

message = ""
for color in colors:
    if color != colors[-1]:
        message += f"{color}/"
    else:
        message += f"{color}"

user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color: {message}").lower()

if user_bet:
    game_on = True

while game_on:
    for turtle in turtles:
        turtle.forward((random.randint(0, 10)))
        if turtle.xcor() > 215:
            game_on = False
            if turtle.pencolor() == user_bet:
                print(f"You win, the turtle {turtle.color()[0]} is the winner!")
            else:
                print(f"You loose, the turtle {turtle.color()[0]} is the winner!")

# def move_forwards():
#     tim.penup()
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.penup()
#     tim.backward(10)
#
#
# def turn_left():
#     tim.left(10)
#
#
# def turn_right():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.home()
#
#
# screen.listen()
# screen.onkey(fun=move_forwards, key="w")
# screen.onkey(fun=move_backwards, key="s")
# screen.onkey(fun=turn_left, key="a")
# screen.onkey(fun=turn_right, key="d")
# screen.onkey(fun=clear, key="c")
screen.exitonclick()


