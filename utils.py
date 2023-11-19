from player import Player

def handle_movement(*keys, player: Player):
    (w,a,s,d) = keys

    player.set_direction(0,0)

    if w.down:
        player.set_direction(0,1)
    if s.down:
        player.set_direction(0,-1)
    if a.down:
        player.set_direction(-1,0)
    if d.down:
        player.set_direction(1,0)
