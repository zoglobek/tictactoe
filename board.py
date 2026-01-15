places = {1: '1', 2: '2', 3: '3',
          4: '4', 5: '5', 6: '6',
          7: '7', 8: '8', 9: '9'}



def checks():
    #Rows
    row_1 = [places[1],places[2], places[3]]
    row_2 = [places[4],places[5], places[6]]
    row_3 = [places[7],places[8], places[9]]
    all_rows = row_1 ,row_2, row_3
    #Columns
    column_1 = [places[1],places[4], places[7]]
    column_2 = [places[2],places[5], places[8]]
    column_3 = [places[3],places[6], places[9]]
    all_columns = column_1, column_2, column_3

    #Diagonals
    diagonal_1 = [places[1],places[5], places[9]]
    diagonal_2 = [places[3],places[5], places[7]]

    all_tiles = [places[1], places[2], places[3],
                 places[4], places[5], places[6],
                 places[7], places[8], places[9]]
    return row_1, row_2, row_3, column_1, column_2, column_3, diagonal_1, diagonal_2, all_tiles, all_rows, all_columns

def board_draw():
        BOARD = (f"|{places[1]}|{places[2]}|{places[3]}|\n"
                 f"|{places[4]}|{places[5]}|{places[6]}|\n"
                 f"|{places[7]}|{places[8]}|{places[9]}|\n"
                 )
        print(BOARD)



if __name__ == "__main__":
    board_draw()
    checks()