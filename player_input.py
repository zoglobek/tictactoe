from board import places
X = "\033[1;31mX"
O = "\033[1;34mO"

def player_input(CURRENT_PLAYER):
    while True:
        tile = int(input(f"{CURRENT_PLAYER} Please enter a Tile number:\n"))
        if tile in range(1,10):
            return (tile)
        else:
            print("Invalid input")


def who_is_player(CURRENT_PLAYER):
    print(CURRENT_PLAYER)



def switch_player(CURRENT_PLAYER):
    if CURRENT_PLAYER == X:
        CURRENT_PLAYER = O
        who_is_player(CURRENT_PLAYER)
        return CURRENT_PLAYER
    else:
        CURRENT_PLAYER = X
        who_is_player(CURRENT_PLAYER)
        return CURRENT_PLAYER




if __name__ == "__main__":
    # ...
    CURRENT_PLAYER = X
    print(player_input(CURRENT_PLAYER))
