
BOARD = "[1|2|3]\n[4|5|6]\n[7|8|9]"

places = {1: '1', 2: '2', 3: '3',
          4: '4', 5: '5', 6: '6',
          7: '7', 8: '8', 9: '9'}

def update_of_set_tiles(BOARD, places):

    for place in places.keys():
        for spot in BOARD:
            if str(place) != spot:
                spot = places.get(place)
    return spot

if __name__ == "__main__":
        print(update_of_set_tiles(BOARD, places))