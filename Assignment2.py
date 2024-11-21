import tkinter as tk


# Initialize the main application window
root = tk.Tk()
root.title("Tic Tac Toe")


# Global variables
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = []


# Function to handle a player's turn
def handle_click(row, col):
    global current_player
    if board[row][col] == "":  # Check if the cell is empty
# Update the board and button text
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        
# Check for a winner
        if check_winner():
            display_winner(current_player)
        else:
# Switch players
            current_player_label.config(text=f"Player {current_player}'s Turn")
            current_player = "O" if current_player == "X" else "X"


# Function to check if a player has won
def check_winner():
# Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
# Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False


# Function to display the winner
def display_winner(winner):
    current_player_label.config(text=f"Player {winner} Wins!")
 # Disable all buttons
    for row in buttons:
        for button in row:
            button.config(state="disabled")


# Function to reset the game
def reset_game():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    current_player_label.config(text="Player X's Turn")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")


# Create the game board
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", font=("Arial", 24), height=2, width=5,
                           command=lambda r=i, c=j: handle_click(r, c))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# Add label to indicate the current player's turn
current_player_label = tk.Label(root, text="Player X's Turn", font=("Arial", 14))
current_player_label.grid(row=3, column=0, columnspan=3)

# Add a reset button
reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

# Start the main event loop
root.mainloop()