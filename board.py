places = {1: '1', 2: '2', 3: '3',
          4: '4', 5: '5', 6: '6',
          7: '7', 8: '8', 9: '9'}

#Rows
row_1 = [places[1],places[2], places[3]]
row_2 = [places[4],places[5], places[6]]
row_3 = [places[7],places[8], places[9]]

#Columns
column_1 = [places[1],places[4], places[7]]
column_2 = [places[2],places[5], places[8]]
column_3 = [places[3],places[6], places[9]]

#Diagonals
Diagonal_1 = [places[1],places[5], places[9]]
Diagonal_2 = [places[3],places[5], places[7]]


def board_draw():
        BOARD = (f"|{places[1]}|{places[2]}|{places[3]}|\n"
                 f"|{places[4]}|{places[5]}|{places[6]}|\n"
                 f"|{places[7]}|{places[8]}|{places[9]}|\n"
                 )
        print(BOARD)



if __name__ == "__main__":
    board_draw()
    print(row_1)
    print(Diagonal_1)
    print(column_1)
    print(row_3)