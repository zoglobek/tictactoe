from board import BOARD
from logic import is_gameover


def turn():
    ...



if __name__ == "__main__":
    while is_gameover():
        turn()
        print(BOARD)