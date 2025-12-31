from board import board_draw, places,  row_1, row_2, row_3, column_2, column_3, column_1, diagonal_1, diagonal_2, all_tiles
from player_input import  X, O, switch_player
from logic import is_tile_set
from logic import check_winner


def turn(CURRENT_PLAYER, diagonal_1, diagonal_2, column_1, column_2, column_3, row_1, row_2, row_3, all_tiles):
    while True:
        board_draw()
        is_tile_set(CURRENT_PLAYER)
        if check_winner(diagonal_1, diagonal_2, column_1, column_2, column_3, row_1, row_2, row_3, all_tiles):
            print("Game Over")
            return False
        board_draw()
        CURRENT_PLAYER = switch_player(CURRENT_PLAYER)




if __name__ == "__main__":
    print(f"welcome to a game of Tic Tack Toe {X} , {O}")
    CURRENT_PLAYER = X
    turn(CURRENT_PLAYER, diagonal_1, diagonal_2, column_1, column_2, column_3, row_1, row_2, row_3, all_tiles)