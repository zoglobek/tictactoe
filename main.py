from logic import is_gameover
from board import board_draw
from player_input import player_input, X, O, switch_player
from logic import is_tile_set


def turn():

    while True:
        board_draw()
        is_tile_set()
        switch_player()
        board_draw()
        is_tile_set()
        switch_player()
        board_draw()


if __name__ == "__main__":
    print(f"welcome to a game of Tic Tack Toe {X} , {O}")
    while True:
        turn()