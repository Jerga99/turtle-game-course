
from player import Player
from window import Window
from game_time import GameTime
import globals as g

def start_game():
    player = Player()
    window = Window()
    last_frame_time = 0

    def move_up():
        player.set_direction(0, 1)

    def move_down():
        player.set_direction(0, -1)

    def move_left():
        player.set_direction(-1, 0)

    def move_right():
        player.set_direction(1, 0)

    window.screen.onkeypress(move_up, 'w')
    window.screen.onkeypress(move_down, 's')
    window.screen.onkeypress(move_left, 'a')
    window.screen.onkeypress(move_right, 'd')

    def update_loop():
        nonlocal last_frame_time
        time_now = GameTime.get_time_now()
        GameTime.delta_time = time_now - last_frame_time

        player.update()
        window.screen.update()

        last_frame_time = time_now
        window.screen.ontimer(update_loop, g.FRAME_TIME_MS)

    last_frame_time = GameTime.get_time_now()
    update_loop()

    window.screen.listen()
    window.screen.mainloop()

start_game()
