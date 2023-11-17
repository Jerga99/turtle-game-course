from player import Player
from window import Window

player = Player()
window = Window()

def move_up():
    new_y = player.ycor() + 20
    player.setpos(player.xcor(), new_y)

def move_down():
    new_y = player.ycor() - 20
    player.setpos(player.xcor(), new_y)

def move_left():
    new_x = player.xcor() - 20
    player.setpos(new_x, player.ycor())

def move_right():
    new_x = player.xcor() + 20
    player.setpos(new_x, player.ycor())

window.screen.onkeypress(move_up, 'w')
window.screen.onkeypress(move_down, 's')
window.screen.onkeypress(move_left, 'a')
window.screen.onkeypress(move_right, 'd')

window.screen.listen()
window.screen.mainloop()
