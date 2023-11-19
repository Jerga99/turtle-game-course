
import math
from turtle import Turtle, Vec2D
from game_time import GameTime

def magnitude(vector: Vec2D):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)

def normalize(vector: Vec2D, mag: float):
    if mag > 0:
        return Vec2D(vector[0] / mag, vector[1] / mag)

    return vector

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('#3ff6ff')
        self.shape('turtle')
        self.speed(0)
        self.penup()
        self.direction = Vec2D(0,0)
        self.movement_speed = 200 # pixels per second

    def set_direction(self, direction: Vec2D):
        self.direction = direction

    def move(self):
        position = self.pos()
        mag = magnitude(self.direction)
        normalized_dir = normalize(self.direction, mag)
        movement = normalized_dir * (self.movement_speed * GameTime.delta_time)

        target_angle = self.towards(self.pos() + normalized_dir)
        self.setheading(target_angle)

        self.setpos(position + movement)

    def update(self):
        self.move()

