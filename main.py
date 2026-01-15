from board import board_draw, places, checks
from player_input import  X, O, switch_player
from logic import is_tile_set
from logic import check_winner
from logic import is_gameover


def turn(CURRENT_PLAYER):
    while True:
        board_draw()
        is_tile_set(CURRENT_PLAYER)
        board_draw()
        CURRENT_PLAYER = switch_player(CURRENT_PLAYER)
        checks()
        if check_winner():
            break




if __name__ == "__main__":
    print(f"welcome to a game of Tic Tack Toe {X} , {O}")
    CURRENT_PLAYER = X
    turn(CURRENT_PLAYER)
    is_gameover()