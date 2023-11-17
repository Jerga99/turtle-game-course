
from turtle import Turtle, Vec2D

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('#3ff6ff')
        self.shape('turtle')
        self.speed(0)
        self.penup()
        self.direction = Vec2D(0,0)

    def set_direction(self, x: float, y: float):
        self.direction = Vec2D(x,y)

    def move(self):
        self.setpos(self.pos() + self.direction)

    def update(self):
        self.move()

