from player_input import player_input, X, O
from board import places, row_1, row_2, row_3, column_2, column_3, column_1, diagonal_1, diagonal_2, all_tiles

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

def three_in_row(row_1, row_2, row_3):
    all_rows = row_1, row_2, row_3
    three_x
    three_o
    for row in all_rows:
        if row == three_x:
            return X
        elif row == three_o:
            return O

def three_in_coulmn(column_1, column_2, column_3):
    all_columns = column_1, column_2, column_3
    three_x
    three_o
    for column in all_columns:
        if column == three_x:
            return X
        elif column == three_o:
            return O


def three_diagonal(diagonal_1, diagonal_2):
    all_diagonals = diagonal_1, diagonal_2
    three_x
    three_o
    for diagonal in all_diagonals:
        if diagonal == three_x:
            return X
        elif diagonal == three_o:
            return O

def out_of_tiles(all_tiles):
    for tile in all_tiles:
        if tile.isdigit():
            return False
    return True


def check_winner(diagonal_1, diagonal_2, column_1, column_2, column_3, row_1, row_2, row_3, all_tiles):
    if three_diagonal(diagonal_1, diagonal_2):
        print(three_diagonal(diagonal_1, diagonal_2))
        return True
    elif three_in_coulmn(column_1, column_2, column_3):
        print(three_in_coulmn(column_1, column_2, column_3))
        return True
    elif three_in_row(row_1, row_2, row_3):
        print(three_in_row(row_1, row_2, row_3))
        return True
    elif out_of_tiles(all_tiles):
        print("TIE")
        return True




def is_gameover():
    ...



if __name__ == "__main__":
    ...