from turtle import Turtle
import random


tim = Turtle()
tim.shape("turtle")

for _ in range(3):
    tim.color("black")
    tim.fd(100)
    tim.lt(120)

for _ in range(4):
    tim.color("blue")
    tim.fd(100)
    tim.lt(90)

for _ in range(5):
    tim.color("red")
    tim.fd(100)
    tim.lt(72)

for _ in range(6):
    tim.color("green")
    tim.fd(100)
    tim.lt(60)

for _ in range(7):
    tim.color("pink")
    tim.fd(100)
    tim.lt(51.42)

for _ in range(8):
    tim.color("orange")
    tim.fd(100)
    tim.lt(45)

for _ in range(9):
    tim.color("purple")
    tim.fd(100)
    tim.lt(40)

#Other method for doing the same:

tin = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360/num_sides
    
    for _ in range(num_sides):
        tin.forward(100)
        tin.right(angle)

for shapes_side in range(3, 10):
    tin.color(random.choice(colours))
    draw_shape(shapes_side)
