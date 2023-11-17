
from turtle import Turtle

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('#3ff6ff')
        self.shape('turtle')
        self.speed(0)
        self.penup()
        self.direction: tuple[float, float] = (1,0)

    def update(self):
        self.setpos(self.pos() + self.direction)
