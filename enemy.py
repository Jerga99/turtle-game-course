from game_entity import GameEntity
from game_time import GameTime

class Enemy(GameEntity):
    def __init__(self, target: GameEntity):
        super().__init__()
        self.target = target
        self.setpos(200,200)
        self.timer = 0
        self.jump_interval = 3

    def follow_target(self):
        target_post = self.target.pos()
        new_heading = self.towards(target_post)
        self.setheading(new_heading)
        self.forward(self.movement_speed * GameTime.delta_time)

    def update(self):
        self.timer += GameTime.delta_time

        if self.timer >= self.jump_interval:
            self.timer = 0
            jump_position = self.target.pos() + (70,70)
            # self.teleport(jump_position[0], jump_position[1])
            self.teleport(*jump_position)


        self.follow_target()
