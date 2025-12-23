import tkinter as tk
from player_input import CURRENT_PLAYER, curr_player_color
from logic import game_restart


BOARD = [[0,0,0,],
         [0,0,0],
         [0,0,0]]


def board():
    # COLOR SCHEME
    black = "#000000"
    lime = "#BBF90F"
    gray = "#808080"
    white = "#FFFFFF"
    yellow = "#FFFF00"
    blue = "#000080"
    red = "#FF0000"
    #gui setup
    window = tk.Tk()
    window.title("TIC TAC TOE")
    window.resizable(False,False)
    frame = tk.Frame(window, bg=gray)
    label = tk.Label(frame, text=(f"Current player is: {CURRENT_PLAYER}"), background=gray, foreground=(curr_player_color()), font=("Arial", 20))
    label.grid(row=0, column=0, columnspan=3, sticky="we")

    for row in range(3):
        for column in range(3):
            BOARD[row][column] = tk.Button(frame, text="", font=("Arial", 50, "bold"), background=gray,foreground=lime , width=4, height=1,
                                           command=set_tile(row,column))
            BOARD[row][column].grid(row=row+1, column=column)

    button_restart = tk.Button(frame, text="Restart Game", font=("Arial", 30, "bold"), background=gray, foreground=black, command=game_restart)
    button_restart.grid(row=4, column=0, columnspan=3, sticky="we")
    frame.pack()
    window.mainloop()

if __name__ == "__main__":
    ...