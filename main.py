from player import Player
from window import Window

player = Player()
window = Window()

# def move_up(distance: int):
#     def move():
#         player.forward(distance)

#     return move

# window.screen.onkeypress(move_up(400), 'w')

def move_up():
    new_y = player.ycor() + 20
    player.setpos(player.xcor(), new_y)

window.screen.onkeypress(move_up, 'w')

window.screen.listen()
window.screen.mainloop()
