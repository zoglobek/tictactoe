from logic import is_gameover
from board import board_draw
import player_input


def turn():
    while True:
        board_draw()
        player_input.player_input()
        player_input.switch_player()
        board_draw()
        player_input.player_input()
        player_input.switch_player()
        board_draw()


if __name__ == "__main__":
    print(f"welcome to a game of Tic Tack Toe {player_input.X} , {player_input.O}")
    while True:
        turn()