# from turtle import *
# import turtle
from turtle import Turtle
import random

t = Turtle()

t.speed(5)

for i in range(20):
    distance = random.randint(50, 100)
    angle = random.randint(0, 90)
    t.left(angle)
    t.fd(distance)

input('Press Any Key: ')
