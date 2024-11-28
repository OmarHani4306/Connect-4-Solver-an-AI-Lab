import tkinter as tk
from tkinter import messagebox
import numpy as np
import math

# Constants
ROWS, COLS = 6, 7
PLAYER, AI = 1, 2
EMPTY = 0

class ConnectFourGUI:
    def __init__(self, root, use_alpha_beta):
        self.root = root
        self.use_alpha_beta = use_alpha_beta
        self.board = np.zeros((ROWS, COLS), dtype=int)
        self.turn = PLAYER
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=COLS * 100, height=ROWS * 100, bg="blue")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.handle_click)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                x0, y0 = c * 100, r * 100
                x1, y1 = x0 + 100, y0 + 100
                color = "white"
                if self.board[r, c] == PLAYER:
                    color = "red"
                elif self.board[r, c] == AI:
                    color = "yellow"
                self.canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill=color)

    def handle_click(self, event):
        if self.turn != PLAYER:
            return

        col = event.x // 100
        if not self.is_valid_location(col):
            return

        row = self.get_next_open_row(col)
        self.board[row][col] = PLAYER
        self.draw_board()

        if self.check_win(PLAYER):
            messagebox.showinfo("Game Over", "You win!")
            self.reset_game()
            return

        self.turn = AI
        self.root.after(500, self.ai_move)

    def ai_move(self):
        col, _ = self.minimax(self.board, 5, -math.inf, math.inf, True) if self.use_alpha_beta else self.minimax(self.board, 5, None, None, True)
        if self.is_valid_location(col):
            row = self.get_next_open_row(col)
            self.board[row][col] = AI
            self.draw_board()

        if self.check_win(AI):
            messagebox.showinfo("Game Over", "AI wins!")
            self.reset_game()
            return

        self.turn = PLAYER

    def reset_game(self):
        # self.board = np.zeros((ROWS, COLS), dtype=int)
        # self.turn = PLAYER
        # self.draw_board()
        self.root.destroy()
        
    def is_valid_location(self, col):
        return self.board[0][col] == EMPTY

    def get_next_open_row(self, col):
        for r in range(ROWS - 1, -1, -1):
            if self.board[r][col] == EMPTY:
                return r

    def check_win(self, piece):
        # Check horizontal locations
        for r in range(ROWS):
            for c in range(COLS - 3):
                if all(self.board[r, c:c+4] == piece):
                    return True
        # Check vertical locations
        for r in range(ROWS - 3):
            for c in range(COLS):
                if all(self.board[r:r+4, c] == piece):
                    return True
        # Check positive diagonals
        for r in range(ROWS - 3):
            for c in range(COLS - 3):
                if all(self.board[r+i, c+i] == piece for i in range(4)):
                    return True
        # Check negative diagonals
        for r in range(3, ROWS):
            for c in range(COLS - 3):
                if all(self.board[r-i, c+i] == piece for i in range(4)):
                    return True
        return False

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        valid_locations = [c for c in range(COLS) if self.is_valid_location(c)]
        is_terminal = self.check_win(PLAYER) or self.check_win(AI) or len(valid_locations) == 0

        if depth == 0 or is_terminal:
            if self.check_win(AI):
                return None, 100000000000000
            elif self.check_win(PLAYER):
                return None, -100000000000000
            else:
                return None, 0

        if maximizing_player:
            value = -math.inf
            column = valid_locations[0]
            for col in valid_locations:
                row = self.get_next_open_row(col)
                b_copy = board.copy()
                b_copy[row][col] = AI
                new_score = self.minimax(b_copy, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                if alpha is not None:
                    alpha = max(alpha, value)
                if beta is not None and alpha >= beta:
                    break
            return column, value
        else:
            value = math.inf
            column = valid_locations[0]
            for col in valid_locations:
                row = self.get_next_open_row(col)
                b_copy = board.copy()
                b_copy[row][col] = PLAYER
                new_score = self.minimax(b_copy, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                if beta is not None:
                    beta = min(beta, value)
                if alpha is not None and alpha >= beta:
                    break
            return column, value


def start_game(welcome_window, use_alpha_beta):
    """Closes the welcome window and starts the main game."""
    root = tk.Tk()
    root.title("Connect Four")
    root.geometry("800x600")
    
    ConnectFourGUI(root, use_alpha_beta)

    root.mainloop()

def show_welcome_window():
    """Displays the welcome window with a checkbox for Alpha-Beta Pruning."""
    # Create a child window for the welcome message
    welcome_window = tk.Tk()
    welcome_window.title("Welcome to Connect Four")
    welcome_window.geometry("400x300")
    # welcome_window.transient(root)  # Keep it on top of the main game window

    # Welcome message
    tk.Label(welcome_window, text="Welcome to Connect Four!", font=("Arial", 16)).pack(pady=20)

    # AI type selection with checkbox
    tk.Label(welcome_window, text="AI Type:", font=("Arial", 12)).pack(pady=10)
    use_alpha_beta = tk.BooleanVar(value=True)  # Default: Alpha-Beta Pruning enabled

    tk.Checkbutton(welcome_window, text="Enable Alpha-Beta Pruning", font=("Arial", 10),
                   variable=use_alpha_beta, onvalue=True, offvalue=False).pack(anchor="w", padx=50)

    # Start Game button
    tk.Button(welcome_window, text="Start Game", font=("Arial", 14),
              command=lambda: start_game(welcome_window, use_alpha_beta.get())).pack(pady=20)
    welcome_window.mainloop()

if __name__ == "__main__":
    show_welcome_window()

