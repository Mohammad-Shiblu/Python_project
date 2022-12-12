import turtle as t
import random
t.colormode(255)
color_list = [(135, 164, 199), (223, 151, 105), (31, 44, 63), (200, 137, 148), (160, 61, 51), (235, 212, 93), (49, 100, 139), (138, 181, 162), (147, 64, 72), (56, 49, 47), (161, 32, 30), (62, 115, 100), (228, 165, 171), (51, 40, 43), (169, 29, 33), (210, 86, 76), (236, 167, 156), (34, 60, 54), (16, 95, 70), (34, 60, 105), (171, 188, 219), (191, 101, 109), (109, 127, 155), (174, 200, 191), (36, 149, 206), (20, 83, 104)]
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(220)
tim.forward(300)
tim.setheading(0)
dot_count = 100

for d in range(1, dot_count+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if (d % 10 == 0):
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        
screen = t.Screen()
screen.exitonclick()
