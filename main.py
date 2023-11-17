from player import Player
from window import Window

def start_game():
    player = Player()
    window = Window()

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
        player.update()
        window.screen.ontimer(update_loop, 10)

    update_loop()

    window.screen.listen()
    window.screen.mainloop()

start_game()
