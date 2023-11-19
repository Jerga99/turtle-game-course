
from turtle import Vec2D
from text import Text

class UI:
    def __init__(self) -> None:
        self.restart_text = Text('Restart?', Vec2D(0,0))

        self.accept_btn = Text('', Vec2D(0, -30))
        self.accept_btn.shape('square')
        self.accept_btn.shapesize(2, 5)
        self.accept_btn.color('green')

        self.decline_btn = Text('', Vec2D(0, -80))
        self.decline_btn.shape('square')
        self.decline_btn.shapesize(2, 5)
        self.decline_btn.color('red')

    def show_gameover(self):
        self.restart_text.show_text()
        self.accept_btn.showturtle()
        self.decline_btn.showturtle()

