from player_input import player_input, X, O
from board import places, checks

three_x = [X, X, X]
three_o = [O, O, O]


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

    *_, all_rows, _ = checks()
    three_x
    three_o
    for row in all_rows:
        if row == three_x:
            return X
        elif row == three_o:
            return O

def three_in_coulmn():
    *_, all_columns  = checks()
    three_x
    three_o
    for column in all_columns:
        if column == three_x:
            return X
        elif column == three_o:
            return O


def three_diagonal():
    *_, diagonal_1, diagonal_2, _, _, _ = checks()
    all_diagonals = diagonal_1, diagonal_2
    three_x
    three_o
    for diagonal in all_diagonals:
        if diagonal == three_x:
            return X
        elif diagonal == three_o:
            return O

def out_of_tiles():
    *_, all_tiles, _, _ = checks()
    for tile in all_tiles:
        if tile.isdigit():
            return False
    return True


def check_winner():
    row_1, row_2, row_3, column_1, column_2, column_3, diagonal_1, diagonal_2, all_tiles, all_rows, all_columns  = checks()
    if three_diagonal():
        print(f"The winner is {three_diagonal()}")
        return True
    elif three_in_coulmn():
        print(f"The winner is {three_in_coulmn()}")
        return True
    elif three_in_row():
        print(f"The winner is {three_in_row()}")
        return True
    elif out_of_tiles():
        print("TIE")
        return True




def is_gameover():
    if check_winner():
        print("Game Over")




if __name__ == "__main__":
    ...
    # column_1 = three_o
    # print(three_in_coulmn(column_1, column_2, column_3))
    # all_tiles = [X, O, X,
    #              O, X, O,
    #              O, X, O]
    # print(out_of_tiles(all_tiles))