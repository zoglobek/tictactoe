from board import places
X = "\033[1;31mX"
O = "\033[1;34mO"
CURRENT_PLAYER = X


def player_input():
    global places
    global CURRENT_PLAYER
    tile = input(f"{CURRENT_PLAYER} Please enter a Tile number:\n")
    places.update({int(tile):CURRENT_PLAYER})




def switch_player(CURRENT_PLAYER):
    if CURRENT_PLAYER == X:
        CURRENT_PLAYER = O
        return CURRENT_PLAYER
    elif CURRENT_PLAYER == O:
         CURRENT_PLAYER = X
         return CURRENT_PLAYER




if __name__ == "__main__":
    ...