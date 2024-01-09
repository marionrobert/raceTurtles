from turtle import Turtle, Screen
import random

#  initialisation du style
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")

# initialisation des variables nécessaires à la préparation du jeu
colors = ["red", "green", "blue", "orange", "pink", "yellow"]
turtles = []
y_positions = [-70, -40, -10, 20, 50, 80]

# création et configuration de l'interface 
screen = Screen()
screen.setup(width=550, height=450)
screen.title("Turtles race")

# création du tableau des scores
scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0, 120)

# création des tortues et positionnement sur la ligne de départ
for n in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[n])
    turtles.append(new_turtle)

# création du prompt de récupération du pari du joueur
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
                # print(f"You win, the turtle {turtle.color()[0]} is the winner!")
                scoreboard.write(f"You win, the turtle {turtle.color()[0]} is the winner!", align=ALIGNMENT, font=FONT)
            else:
                # print(f"You loose, the turtle {turtle.color()[0]} is the winner!")
                scoreboard.write(f"You loose, the turtle {turtle.color()[0]} is the winner!", align=ALIGNMENT, font=FONT)


screen.exitonclick()
