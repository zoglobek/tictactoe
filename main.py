from board import board_draw
from player_input import  X, O, switch_player
from logic import is_tile_set
def turn(CURRENT_PLAYER):
    while True:
        board_draw()
        is_tile_set(CURRENT_PLAYER)
        CURRENT_PLAYER = switch_player(CURRENT_PLAYER)
        board_draw()
        is_tile_set(CURRENT_PLAYER)
        CURRENT_PLAYER = switch_player(CURRENT_PLAYER)



if __name__ == "__main__":
    print(f"welcome to a game of Tic Tack Toe {X} , {O}")
    CURRENT_PLAYER = X
    turn(CURRENT_PLAYER)