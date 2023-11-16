
from turtle import Turtle

class Player:
    def __init__(self) -> None:
        self.t = Turtle()
        self.t.color('#3ff6ff')
        self.t.speed(3)


class MyTurtle:
    def __init__(self) -> None:
        self.a = 10
        self.b = 20
        self.c = 30

    def method_1(self):
        pass

    def method_2(self):
        pass

    def method_3(self):
        pass

    def method_4(self):
        pass


class MyPlayer(MyTurtle):
    def __init__(self) -> None:
        super().__init__()
        self.x = 40
        self.a = 100
        self.b = 200

    def method_X(self):
        pass

    def method_Y(self):
        pass

    def method_Z(self):
        pass

player = MyPlayer()

print(player.a)
print(player.b)
print(player.x)
