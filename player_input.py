from board import places

X = "\033[1;31mX"
O = "\033[1;34mO"
global CURRENT_PLAYER
CURRENT_PLAYER = X


def player_input():
    tile = input("Please enter a Tile number:\n")
    return places.update({tile:CURRENT_PLAYER})




def switch_player(CURRENT_PLAYER):
    if CURRENT_PLAYER == X:
        CURRENT_PLAYER = O
        return CURRENT_PLAYER
    elif CURRENT_PLAYER == O:
         CURRENT_PLAYER = X
         return CURRENT_PLAYER


def is_tile_set(tile,set_tiles:list):
    if tile ==...:
        ...

if __name__ == "__main__":
    print(X, O)