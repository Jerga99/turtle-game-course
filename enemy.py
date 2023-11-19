from game_entity import GameEntity
from game_time import GameTime

class Enemy(GameEntity):
    def __init__(self, target: GameEntity):
        super().__init__()
        self.target = target
        self.setpos(200,200)

    def follow_target(self):
        target_post = self.target.pos()
        new_heading = self.towards(target_post)
        self.setheading(new_heading)
        self.forward(self.movement_speed * GameTime.delta_time)

    def update(self):
        self.follow_target()
