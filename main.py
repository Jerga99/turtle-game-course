from player import Player
from window import Window

player = Player()
window = Window()

player.setpos(-400, 300)
player.setpos(400, 300)
# player.setpos(0,0)
player.home()

player.setpos(-400, -300)
player.setpos(400, -300)
player.home()

window.screen.mainloop()
