from player import Player
from window import Window

player = Player()
window = Window()

player.setpos(200, 0)
player.setpos(200, 100)
player.setpos(0, 100)
player.setpos(0, 0)
player.setpos(100, 100)
player.setpos(200, 0)

window.screen.mainloop()
