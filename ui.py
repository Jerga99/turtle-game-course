
from turtle import Vec2D
from text import Text

class UI:
    def __init__(self) -> None:
        self.restart_text = Text('Restart?', Vec2D(0,0))

    def show_gameover(self):
        self.restart_text.show_text()
