places = {1: '1', 2: '2', 3: '3',
          4: '4', 5: '5', 6: '6',
          7: '7', 8: '8', 9: '9'}
def board_draw():
        BOARD = (f"|{places[1]}|{places[2]}|{places[3]}|\n"
                 f"|{places[4]}|{places[5]}|{places[6]}|\n"
                 f"|{places[7]}|{places[8]}|{places[9]}|\n"
                 )
        print(BOARD)



if __name__ == "__main__":
    board_draw()