import random
import turtle

tim = turtle.Turtle()
screen = turtle.Screen()
tim.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r,g,b)
    return color_tuple

def draw_spirograph(size_of_gap):
  for _ in  range(int(360/size_of_gap)):
      tim.color(random_color())
      tim.circle(_)
      _ /= 10
      tim.setheading(tim.heading()+10)
draw_spirograph(1)
tim.getscreen()
screen.exitonclick()