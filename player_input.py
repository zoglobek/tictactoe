from board import places
X = "\033[1;31mX"
O = "\033[1;34mO"

def player_input(CURRENT_PLAYER):
    global places
    while True:
        tile = input(f"{CURRENT_PLAYER} Please enter a Tile number:\n")
        if tile.isdigit():
            return int(tile)
        else:
            print("Invalid input")


def who_is_player(CURRENT_PLAYER):
    print(CURRENT_PLAYER)



def switch_player():
    global CURRENT_PLAYER
    if CURRENT_PLAYER == X:
        CURRENT_PLAYER = O
        return CURRENT_PLAYER
    else:
        CURRENT_PLAYER = X
        return CURRENT_PLAYER




if __name__ == "__main__":
    ...
    # CURRENT_PLAYER = X
    # print(switch_player())
    # print(switch_player())
    # print(switch_player())
    # who_is_player(CURRENT_PLAYER)
    # print(switch_player())
    # print(switch_player())
