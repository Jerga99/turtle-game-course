# from turtle import *
# import turtle
from turtle import Screen
import random
from player import Player

_player = Player()

screen = Screen()
screen.setup(800, 600)
screen.title('Turtle Battles')
screen.bgcolor('#000000')

for i in range(20):
    distance = random.randint(50, 100)
    angle = random.randint(0, 90)
    _player.t.left(angle)
    _player.t.fd(distance)


screen.mainloop()
