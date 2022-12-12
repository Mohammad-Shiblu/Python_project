from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")

for sides in range(3, 11):
    angles = 360 /sides
    for i in range(sides):
        t.forward(100)
        t.right(angles)
        

screen = Screen()
screen.exitonclick()
