
from turtle import Turtle, Vec2D

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('#3ff6ff')
        self.shape('turtle')
        self.speed(0)
        self.penup()
        self.direction = Vec2D(1,0)

    def move(self):
        self.setpos(self.pos() + self.direction)

    def update(self):
        self.move()

