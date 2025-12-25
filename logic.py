from player_input import player_input, X, O
from board import places

def is_tile_set():
    global CURRENT_PLAYER
    tile = player_input(CURRENT_PLAYER)
    global places
    while places[tile] == X or places[tile] == O:
        print("invalid tile")
        tile = player_input()
    else:
        print("valid")
        places.update({tile: CURRENT_PLAYER})




def is_gameover():
    ...

def check_winner():
    ...
if __name__ == "__main__":
    is_tile_set()