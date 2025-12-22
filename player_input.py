#COLOR SCHEME
black = "#000000"
lime = "#BBF90F"
gray = "#808080"
white = "#FFFFFF"
yellow = "#FFFF00"
blue = "#000080"
red = "#FF0000"

X = "X"
O = "O"
CURRENT_PLAYER = X

def curr_player_color():
    if CURRENT_PLAYER == X:
        player_color = red
    elif CURRENT_PLAYER == O:
        player_color = blue
    return player_color


def switch_player():
    ...
def is_tile_set():
    ...

if __name__ == "__main__":
    ...