import turtle
import random

window = turtle.Screen()
window.bgcolor("#69D9FF") 
myPen = turtle.Turtle()
myPen.speed(10) 

def draw_rectangle(turtle_obj, color, x, y, width, height):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color(color)
    turtle_obj.begin_fill()
    for _ in range(2):
        turtle_obj.forward(width)
        turtle_obj.right(90)
        turtle_obj.forward(height)
        turtle_obj.right(90)
    turtle_obj.end_fill()


def draw_star(turtle_obj, color, x, y, size):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color(color)
    turtle_obj.begin_fill()
    for _ in range(5):
        turtle_obj.forward(size)
        turtle_obj.right(144) 
    turtle_obj.end_fill()


y_position = -100
width = 240
height = 30

draw_rectangle(myPen, "brown", -15, y_position - 40, 30, 40)

while width > 20:
    width = width - random.randint(20, 30) 
    x_position = 0 - width / 2
    draw_rectangle(myPen, "green", x_position, y_position, width, height)
    y_position += height 

draw_star(myPen, "yellow", -10, y_position, 20)


myPen.hideturtle()
turtle.done()
