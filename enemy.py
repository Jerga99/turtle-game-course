from game_entity import GameEntity

class Enemy(GameEntity):
    def __init__(self):
        super().__init__()
        self.setpos(200,200)

    def update(self):
        pass
