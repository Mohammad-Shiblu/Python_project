import turtle as t
import random
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim = t.Turtle()
tim.speed("fastest")
for r in range(0, 360, 5):
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)
    


screen = t.Screen()
screen.exitonclick()