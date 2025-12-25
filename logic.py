from player_input import player_input, X, O, CURRENT_PLAYER
from board import places

def is_tile_set():
    tile = player_input()
    global places
    if not places[tile] == X or not places[tile] == O:
        print("valid")
        places.update({tile: CURRENT_PLAYER})

    else:
        print("invalid")



def is_gameover():
    ...

def check_winner():
    ...
if __name__ == "__main__":
    is_tile_set()