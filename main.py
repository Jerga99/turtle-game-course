from player import Player
from window import Window

player = Player()
window = Window()

def move_up():
    player.forward(20)

window.screen.onkeypress(move_up, 'w')

window.screen.listen()
window.screen.mainloop()
