from turtle import Turtle, Screen

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


