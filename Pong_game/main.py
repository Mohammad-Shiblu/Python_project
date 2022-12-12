import turtle as t
import random as r


is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, green, blue, yellow, orange, purple): ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]

turtle_name = []
y_positions = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0, 6):
    tim = t.Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y = y_positions[turtle_index])
    tim.color(colors[turtle_index])
    turtle_name.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_name:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = r.randint(0, 10)
        turtle.forward(rand_distance)
    
screen.exitonclick()
