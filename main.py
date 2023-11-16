import random
from player import Player
from window import Window

player = Player()
window = Window()

for i in range(20):
    distance = random.randint(50, 100)
    angle = random.randint(0, 90)
    player.left(angle)
    player.fd(distance)


window.screen.mainloop()
