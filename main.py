
from player import Player
from window import Window
from game_time import GameTime
from watched_key import WatchedKey
import globals as g

def start_game():
    player = Player()
    window = Window()

    w = WatchedKey('w')
    a = WatchedKey('a')
    s = WatchedKey('s')
    d = WatchedKey('d')

    def update_loop():
        GameTime.process_time()

        player.set_direction(0,0)

        if w.down:
            player.set_direction(0,1)
        if s.down:
            player.set_direction(0,-1)
        if a.down:
            player.set_direction(-1,0)
        if d.down:
            player.set_direction(1,0)

        player.update()
        window.screen.update()

        window.screen.ontimer(update_loop, g.FRAME_TIME_MS)

    GameTime.init()
    update_loop()

    window.screen.listen()
    window.screen.mainloop()

start_game()
