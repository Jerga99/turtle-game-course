from player import Player
from window import Window
import globals as g

def start_game():
    player = Player()
    window = Window()

    # def move_up():
    #     new_y = player.ycor() + g.DISTANCE_STEP
    #     player.setpos(player.xcor(), new_y)

    # def move_down():
    #     new_y = player.ycor() - g.DISTANCE_STEP
    #     player.setpos(player.xcor(), new_y)

    # def move_left():
    #     new_x = player.xcor() - g.DISTANCE_STEP
    #     player.setpos(new_x, player.ycor())

    # def move_right():
    #     new_x = player.xcor() + g.DISTANCE_STEP
    #     player.setpos(new_x, player.ycor())

    # window.screen.onkeypress(move_up, 'w')
    # window.screen.onkeypress(move_down, 's')
    # window.screen.onkeypress(move_left, 'a')
    # window.screen.onkeypress(move_right, 'd')

    def update_loop():
        player.update()
        window.screen.ontimer(update_loop, 10)

    update_loop()

    window.screen.listen()
    window.screen.mainloop()

start_game()
