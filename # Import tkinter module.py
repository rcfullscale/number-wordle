# Import tkinter module
import tkinter as tk
from tkinter import messagebox

# Create a root window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create a class to represent the game board
class Board(tk.Frame):
    def __init__(self, parent):
        # Initialize the frame
        super().__init__(parent)
        # Create a list of buttons as tiles
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                # Create a button with empty text and a callback function
                button = tk.Button(self, text="", width=5, height=2, font=("Arial", 20),
                                   command=lambda r=i, c=j: self.click(r, c))
                # Add the button to the grid and the row list
                button.grid(row=i, column=j)
                row.append(button)
            # Add the row list to the buttons list
            self.buttons.append(row)

    # Define a method to handle the button click events
    def click(self, row, col):
        # Get the current player and the button
        player = game.get_player()
        button = self.buttons[row][col]
        # Check if the button is empty and the game is not over
        if button["text"] == "" and not game.is_over():
            # Update the button text and the game logic
            button["text"] = player
            game.update(row, col)
            # Check if the game is over
            if game.is_over():
                # Show a message box with the result
                if game.is_tie():
                    messagebox.showinfo("Result", "It's a tie!")
                else:
                    messagebox.showinfo("Result", f"{player} wins!")
            # Switch to the next player
            game.switch_player()

# Create a class to represent the game logic
class Game:
    def __init__(self, player):
        # Initialize the player, the board, and the over flag
        self.player = player
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.over = False

    # Define a method to get the current player
    def get_player(self):
        return self.player

    # Define a method to update the board with the player's move
    def update(self, row, col):
        # Check if the move is valid
        if self.board[row][col] == 0:
            # Update the board with the player's symbol (1 for X, -1 for O)
            if self.player == "X":
                self.board[row][col] = 1
            else:
                self.board[row][col] = -1
            # Check if the game is over
            self.check_over()

    # Define a method to check if the game is over
    def check_over(self):
        # Check for horizontal, vertical, and diagonal wins
        for i in range(3):
            if abs(sum(self.board[i])) == 3:
                self.over = True
                return
            if abs(self.board[0][i] + self.board[1][i] + self.board[2][i]) == 3:
                self.over = True
                return
        if abs(self.board[0][0] + self.board[1][1] + self.board[2][2]) == 3:
            self.over = True
            return
        if abs(self.board[0][2] + self.board[1][1] + self.board[2][0]) == 3:
            self.over = True
            return
        # Check for a tie
        if 0 not in self.board[0] and 0 not in self.board[1] and 0 not in self.board[2]:
            self.over = True
            return

    # Define a method to check if the game is a tie
    def is_tie(self):
        return self.over and 0 in self.board[0] and 0 in self.board[1] and 0 in self.board[2]

    # Define a method to check if the game is over
    def is_over(self):
        return self.over

    # Define a method to switch to the next player
    def switch_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

# Define a function to create a menu
def create_menu():
    # Create a menu bar
    menu_bar = tk.Menu(root)
    # Create a file menu with two commands
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Play Again", command=play_again)
    file_menu.add_command(label="Exit", command=root.destroy)
    # Add the file menu to the menu bar
    menu_bar.add_cascade(label="File", menu=file_menu)
    # Return the menu bar
    return menu_bar

# Define a function to play again
def play_again():
    # Reset the game logic and the board
    global game
    game = Game("X")
    board = Board(root)
    # Add the board to the root window
    board.pack()

# Create two instances of the game logic class, one for each player
game = Game("X")

# Create an instance of the board class
board = Board(root)

# Create a menu and add it to the root window
menu = create_menu()
root.config(menu=menu)

# Add the board to the root window
board.pack()

# Start the main loop
root.mainloop()
