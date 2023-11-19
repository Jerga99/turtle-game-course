from turtle import Turtle

class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('square')
        self.speed(0)
        self.penup()
        self.movement_speed = 200
        self.setpos(200,200)

    def update(self):
        pass
