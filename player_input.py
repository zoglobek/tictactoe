from board import places
X = "\033[1;31mX"
O = "\033[1;34mO"

def player_input(CURRENT_PLAYER):
    while True:
        tile = (input(f"{CURRENT_PLAYER} Please enter a Tile number:\n"))
        if tile.isdigit():
            tile = int(tile)
            if tile in range(1,10):
                return (tile)
            else:
                print("Tile is not in range")
        else:
            print("Invalid input")




def switch_player(CURRENT_PLAYER):
    if CURRENT_PLAYER == X:
        CURRENT_PLAYER = O
        return CURRENT_PLAYER
    else:
        CURRENT_PLAYER = X
        return CURRENT_PLAYER




if __name__ == "__main__":

    #
    CURRENT_PLAYER = X
    print(player_input(CURRENT_PLAYER))
    CURRENT_PLAYER = switch_player(CURRENT_PLAYER)
    print(player_input(CURRENT_PLAYER))
    CURRENT_PLAYER = switch_player(CURRENT_PLAYER)
