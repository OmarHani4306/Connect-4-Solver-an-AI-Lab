import tkinter as tk
from tkinter import messagebox
import numpy as np
import math, random
import importlib


# Constants
ROWS, COLS = 4, 4
PLAYER, AI = 1, 2
EMPTY = 0

class ConnectFourGUI:
    def __init__(self, root, algorithm, k=None):
        self.root = root
        self.algorithm = algorithm
        self.k = k
        self.board = [[str(EMPTY) for _ in range(COLS)] for _ in range(ROWS)]
        self.top_row = [ROWS - 1] * COLS  # Tracks the top-most empty row for each column
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
                if self.board[r][c] == str(PLAYER):
                    color = "red"
                elif self.board[r][c] == str(AI):
                    color = "yellow"
                self.canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill=color)

    def handle_click(self, event):
        if self.turn != PLAYER:
            return

        col = event.x // 100
        if not self.is_valid_location(col):
            messagebox.showerror("Invalid Move", "This column is full. Choose another column.")
            return

        row = self.top_row[col]
        self.board[row][col] = str(PLAYER)
        self.top_row[col] -= 1  # Update the top row tracker
        self.draw_board()

        if self.is_board_full():
            self.end_game()
            return

        self.turn = AI
        self.root.after(500, self.ai_move)


    def ai_move(self):
        # Dynamically import and run the selected algorithm
        module = importlib.import_module(self.algorithm)
        # col, _ = module.run(self.board, self.k)
        col = np.random.choice(COLS)

        while not self.is_valid_location(col):
            # col, _ = module.run(self.board, self.k)
            col = np.random.choice(COLS)
            
        row = self.top_row[col]
        self.board[row][col] = str(AI)
        self.top_row[col] -= 1
        self.draw_board()

        if self.is_board_full():
            self.end_game()
            return

        self.turn = PLAYER

    def is_valid_location(self, col):
        return self.top_row[col] >= 0

    def is_board_full(self):
        return all(self.top_row[c] < 0 for c in range(COLS))

    def count_connected_fours(self, piece):
        count = 0

        # Helper to check bounds and match piece
        def in_bounds_and_matches(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS and self.board[r][c] == str(piece)

        # Traverse board to count connected fours
        for r in range(ROWS):
            for c in range(COLS):
                if self.board[r][c] != str(piece):
                    continue

                # Horizontal
                if c <= COLS - 4 and all(in_bounds_and_matches(r, c + i) for i in range(4)):
                    count += 1

                # Vertical
                if r <= ROWS - 4 and all(in_bounds_and_matches(r + i, c) for i in range(4)):
                    count += 1

                # Positive Diagonal
                if r <= ROWS - 4 and c <= COLS - 4 and all(in_bounds_and_matches(r + i, c + i) for i in range(4)):
                    count += 1

                # Negative Diagonal
                if r >= 3 and c <= COLS - 4 and all(in_bounds_and_matches(r - i, c + i) for i in range(4)):
                    count += 1

        return count

    def end_game(self):
        player_score = self.count_connected_fours(PLAYER)
        ai_score = self.count_connected_fours(AI)

        if player_score > ai_score:
            messagebox.showinfo("Game Over", f"You win! Score: Player {player_score} - AI {ai_score}")
        elif ai_score > player_score:
            messagebox.showinfo("Game Over", f"AI wins! Score: Player {player_score} - AI {ai_score}")
        else:
            messagebox.showinfo("Game Over", f"It's a tie! Score: Player {player_score} - AI {ai_score}")
        
        self.reset_game()

    def reset_game(self):
        self.root.destroy()


def start_game(welcome_window, algorithm, k):
    root = tk.Tk()
    root.title("Connect Four")
    root.geometry("800x600")
    ConnectFourGUI(root, algorithm, k)
    root.mainloop()

def show_welcome_window():
    """Displays the welcome window with options to select an AI algorithm and configure settings."""
    def toggle_k_input():
        """Show or hide the K input field based on the selected algorithm."""
        if algorithm_var.get() == "minimax_with_pruning":
            k_label.pack(pady=5)
            k_entry.pack(pady=5)
        else:
            k_label.pack_forget()
            k_entry.pack_forget()

    def start_game_from_welcome():
        """Starts the game with the selected settings."""
        algorithm = algorithm_var.get()
        k_value = k_entry.get() if algorithm == "minimax_with_pruning" else None
        if algorithm == "minimax_with_pruning" and not k_value.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid integer for K.")
            return
        start_game(welcome_window, algorithm, int(k_value) if k_value else None)

    # Create the welcome window
    welcome_window = tk.Tk()
    welcome_window.title("Welcome to Connect Four")
    welcome_window.geometry("640x360")

    # Welcome message
    tk.Label(welcome_window, text="Welcome to Connect Four!", font=("Arial", 16)).pack(pady=20)

    # Algorithm selection
    tk.Label(welcome_window, text="Choose AI Algorithm:", font=("Arial", 12)).pack(pady=10)
    algorithm_var = tk.StringVar(value="minimax_no_pruning")

    # Algorithm options
    algorithms = [
        ("Minimax without Pruning", "minimax_no_pruning"),
        ("Minimax with Pruning", "minimax_with_pruning"),
        ("Expected Minimax", "expected_minimax")
    ]
    for text, value in algorithms:
        tk.Radiobutton(
            welcome_window, text=text, variable=algorithm_var, value=value,
            font=("Arial", 10), command=toggle_k_input
        ).pack(anchor="w", padx=50)

    # K input field (hidden by default)
    k_label = tk.Label(welcome_window, text="Enter pruning depth (K):", font=("Arial", 10))
    k_entry = tk.Entry(welcome_window)

    # Start game button
    tk.Button(welcome_window, text="Start Game", font=("Arial", 14),
              command=start_game_from_welcome).pack(pady=20)

    welcome_window.mainloop()

if __name__ == "__main__":
    show_welcome_window()

