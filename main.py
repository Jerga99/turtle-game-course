
from player import Player
from window import Window
from game_time import GameTime
from watched_key import WatchedKey
import globals as g

def start_game():
    player = Player()
    window = Window()

    # def move_up():
    #     player.set_direction(0, 1)

    # def move_down():
    #     player.set_direction(0, -1)

    # def move_left():
    #     player.set_direction(-1, 0)

    # def move_right():
    #     player.set_direction(1, 0)

    # onkeypress(move_up, 'w')
    # onkeypress(move_down, 's')
    # onkeypress(move_left, 'a')
    # onkeypress(move_right, 'd')

    space = WatchedKey('space')
    w = WatchedKey('w')

    def update_loop():
        GameTime.process_time()

        print(f'W is down: {w.down}')

        player.update()
        window.screen.update()

        window.screen.ontimer(update_loop, g.FRAME_TIME_MS)

    GameTime.init()
    update_loop()

    window.screen.listen()
    window.screen.mainloop()

start_game()
