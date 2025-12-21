import tkinter as tk
from tictactoe.player_input import CURRENT_PLAYER

BOARD = [[0,0,0,],
         [0,0,0],
         [0,0,0]]
def set_tile(row, column):
    ...


#gui setup
gray = "#808080"
white = "#FFFFFF"
window = tk.Tk()
window.title("TIC TAC TOE")
window.resizable(False,False)
frame = tk.Frame(window)
label = tk.Label(frame, text=("Current player is", CURRENT_PLAYER), background=gray, foreground=white, font=("Arial", 20))
label.grid(row=0, column=0)
for row in range(3):
    for column in range(3):
        BOARD[row][column] = tk.Button(frame, text="", font=("Arial", 50, "bold"), background=gray)
frame.pack(fill="both",expand=True)
window.mainloop()

if __name__ == "__main__":
    ...