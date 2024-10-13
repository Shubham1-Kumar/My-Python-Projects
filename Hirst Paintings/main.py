# import colorgram
# rgb_list = []
# colors = colorgram.extract('hirst.jpg',50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_list.append(new_color)
# print(rgb_list)
import random
import turtle
import turtle as turtle_module

from PIL.ImImagePlugin import number

turtle.colormode(255)
tim = turtle_module.Turtle()
screen = turtle_module.Screen()
color_list = [(239, 229, 212), (202, 160, 106), (130, 161, 190), (218, 228, 239), (241, 222, 232), (72, 99, 138),
              (140, 72, 98), (222, 237, 229), (189, 140, 161), (150, 89, 61), (221, 202, 129), (138, 176, 154),
              (73, 121, 90), (154, 151, 63), (178, 95, 121), (190, 99, 80), (124, 34, 50), (98, 122, 171),
              (91, 149, 116), (219, 174, 193), (50, 55, 100), (163, 208, 189), (177, 187, 216), (225, 176, 167),
              (69, 37, 58), (82, 146, 160), (44, 46, 73), (160, 204, 214), (127, 39, 33), (72, 44, 35), (42, 79, 58),
              (40, 62, 51), (74, 73, 40), (40, 74, 82), (215, 201, 40)]
tim.penup()
tim.speed("fastest")
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots =100

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()


