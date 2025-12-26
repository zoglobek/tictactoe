from player_input import player_input, X, O
from board import places


def is_tile_set(CURRENT_PLAYER):
    tile = player_input(CURRENT_PLAYER)
    while places[tile] == X or places[tile] == O:
        print("invalid tile")
    else:
        print("valid")
        places.update({tile: CURRENT_PLAYER})


def check_winner():
    ...

def is_gameover():
    values = places.values()
    for value in values:
        if value is not value.isdigit():
            check_winner()
    else:
        ...



if __name__ == "__main__":
    ...
    # is_tile_set(CURRENT_PLAYER)