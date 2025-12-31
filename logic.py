from player_input import player_input, X, O
from board import places, row_1, row_2, row_3, column_2, column_3, column_1, diagonal_1, diagonal_2, all_tiles



def is_tile_set(CURRENT_PLAYER):
    while True:
        tile = player_input(CURRENT_PLAYER)
        if places[tile] == X or places[tile] == O:
            print("invalid tile")
        else:
            print("valid")
            places.update({tile: CURRENT_PLAYER})
            break

def three_in_row():
    for place in row_1:
        if place == X or place == O:
            return X
        else:
            return O
    for place in row_2:
        if place == X or place == O:
            return X
        else:
            return O
    for place in row_3:
        if place == X or place == O:
            return X
        else:
            return O
    else:
        return False


def three_in_coulmn():
    for place in column_1:
        if place == X or place == O:
            return X
        else:
            return O
    for place in column_2:
        if place == X or place == O:
            return X
        else:
            return O
    for place in column_3:
        if place == X or place == O:
            return X
        else:
            return O
    else:
        return False


def three_diagonal():
    for place in diagonal_1:
        if place == X or place == O:
            return X
        else:
            return O
    for place in diagonal_2:
        if place == X or place == O:
            return X
        else:
            return O
    else:
        return False


def check_winner():
    ...

def is_gameover():
    if all_tiles:
        check_winner()



if __name__ == "__main__":
    ...
    # is_tile_set(CURRENT_PLAYER)