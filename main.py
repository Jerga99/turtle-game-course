
from turtle import Vec2D
from player import Player
from enemy import Enemy
from text import Text
from window import Window
from game_time import GameTime
from watched_key import WatchedKey
from utils import handle_movement
import globals as g

def start_game():
    player = Player()
    enemy = Enemy(target=player)
    text = Text('Restart?', Vec2D(100,100))
    window = Window()

    w = WatchedKey('w')
    a = WatchedKey('a')
    s = WatchedKey('s')
    d = WatchedKey('d')

    def update_loop():
        GameTime.process_time()

        if g.GAME_OVER:
            # Display some UI informing the player that the game is over
            pass
        else:
            handle_movement(w,a,s,d, player=player)
            player.update()
            enemy.update()

        window.screen.update()
        window.screen.ontimer(update_loop, g.FRAME_TIME_MS)

    GameTime.init()
    update_loop()

    window.screen.listen()
    window.screen.mainloop()

start_game()
