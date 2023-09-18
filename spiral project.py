
import turtle as t
import random
t.colormode(255)

def get_color():
    r = random.randint(0,255)
    p = random.randint(0,255)
    b = random.randint(0,255)
    color = (r , p, b)
    return color

timmy = t.Turtle()
for i in range(50):
    timmy.circle(45)
    timmy.color(get_color())
    timmy.right(10)
