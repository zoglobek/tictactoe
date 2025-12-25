from logic import is_gameover
from board import board_draw
from player_input import player_input, X, O, switch_player
from logic import is_tile_set
from tictactoe.player_input import who_is_player
CURRENT_PLAYER = X

def turn():
    global CURRENT_PLAYER
    while True:
        board_draw()
        is_tile_set()
        switch_player()
        who_is_player(CURRENT_PLAYER)
        board_draw()
        who_is_player(CURRENT_PLAYER)
        is_tile_set(CURRENT_PLAYER)
        who_is_player(CURRENT_PLAYER)
        switch_player()
        who_is_player(CURRENT_PLAYER)
        board_draw()


if __name__ == "__main__":
    print(f"welcome to a game of Tic Tack Toe {X} , {O}")
    turn()