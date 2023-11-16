# from turtle import *
# import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

screen.setup(800, 600)
screen.title('Turtle Battles')
screen.bgcolor('#000000')

t.speed(5)

for i in range(20):
    distance = random.randint(50, 100)
    angle = random.randint(0, 90)
    t.left(angle)
    t.fd(distance)

input('Press Any Key: ')
