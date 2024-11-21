#import the libraries for GUI based Tic tac toe game

import tkinter as tk

#INITIALISE THE MAIN GAME WINDOW

root = tk.Tk()
root.title("Tic Tac Toe")

#create a function to create a 3 by 3 game board with buttons for each block
def create_board():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    for i in range(3):
      for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(root, text="", font=("Arial", 24), height=2, width=5, 
                               command=lambda r=i, c=j: handle_click(r, c))
            button.grid(row=i, column=j)
            row.append(button)
        button.append(row)

