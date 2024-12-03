import tkinter as tk
from minimax_no_pruning import minimax
from minimax_with_pruning import alphabeta_minimax 
from expected_minimax import expectiminimax 
from helpers import *


def draw_triangle(canvas, x, y, size, orientation, color, text):
    """
    Draws a triangle (upward or downward) on the canvas.
    """
    if orientation == 'up':
        points = [x, y - size, x - size, y + size, x + size, y + size]
    else:  # Downward triangle
        points = [x, y + size, x - size, y - size, x + size, y - size]

    canvas.create_polygon(points, fill=color, outline="black")
    canvas.create_text(x, y, text=text, font=("Arial", 10), fill="black")


def draw_circle(canvas, x, y, radius, color, text):
    """
    Draws a circle on the canvas.
    """
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline="black")
    canvas.create_text(x, y, text=text, font=("Arial", 10), fill="black")


def draw_tree(canvas, tree, x, y, level_gap, node_gap, depth=0, size=20):
    """
    Draws the tree recursively on the canvas.
    """
    if tree is None:
        return

    # Determine the node type and draw accordingly
    node_type = tree['type']
    value = tree['value']
    move = tree['move']
    label = f"{node_type.capitalize()}\nValue={value}\nMove={move}"

    if node_type == 'max':
        draw_triangle(canvas, x, y, size, 'up', 'lightblue', label)
    elif node_type == 'min':
        draw_triangle(canvas, x, y, size, 'down', 'lightgreen', label)
    elif node_type == 'chance':
        draw_circle(canvas, x, y, size, 'yellow', label)

    # Draw child nodes and connecting lines
    if 'children' in tree and tree['children']:
        num_children = len(tree['children'])
        child_x_start = x - (num_children - 1) * node_gap // 2

        for i, child in enumerate(tree['children']):
            child_x = child_x_start + i * node_gap
            child_y = y + level_gap

            # Draw the line connecting parent to child
            line_label = f"Move {child['move']} → {child['value']}"
            canvas.create_line(x, y + size, child_x, child_y - size, fill="black", arrow=tk.LAST)
            canvas.create_text((x + child_x) // 2, (y + child_y) // 2, text=line_label, font=("Arial", 8))

            draw_tree(canvas, child, child_x, child_y, level_gap, node_gap, depth + 1, size)


def show_tree_gui(tree):
    """
    Visualizes the tree using Tkinter.
    """
    window = tk.Tk()
    window.title("Tree Visualization")

    canvas = tk.Canvas(window, width=1200, height=800, bg="white")
    canvas.pack()

    draw_tree(canvas, tree, x=600, y=50, level_gap=100, node_gap=150)
    # window.mainloop()

def play_game(algorithm, MAX_DEPTH, columns, rows):
    #change
    state = 0  
    human_player = 2 
    ai_player = 1  
    turn_depth = 0  

    print("Starting Connect 4! You are Player 2 (Human).")
    while not is_terminal(state, turn_depth, MAX_DEPTH, columns, rows):  
        # Human Turn
        valid = valid_moves(state, columns, rows)
        print(f"Valid moves: {valid}")
        while True:
            try:
                human_move = int(input(f"Enter your move (0-{columns - 1}): "))
                if human_move in valid:
                    break
                print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid column number.")
        state = apply_move(state, human_move, human_player, columns, rows)

        turn_depth += 1  

        # Check if the game ends after Human's turn
        if is_terminal(state, turn_depth, MAX_DEPTH, columns, rows):
            break

        # AI Turn
        print("AI is thinking...")
        if algorithm == "minimax":
            _, best_move, tree = minimax(state, turn_depth, True, MAX_DEPTH, columns, rows)
        elif algorithm == "alphabeta":
            _, best_move, tree = alphabeta_minimax(state, turn_depth, -float('inf'), float('inf'), True, MAX_DEPTH, columns, rows)
        elif algorithm == "expectiminimax":
            _, best_move, tree = expectiminimax(state, turn_depth, True,'max', MAX_DEPTH, columns, rows)
        else:
            raise ValueError("Invalid algorithm. Choose 'minimax', 'alphabeta', or 'expectiminimax'.")

        state = apply_move(state, best_move, ai_player, columns, rows)
        print(f"AI chose column {best_move}.")
        turn_depth += 1  

        
        show_tree_gui(tree)

    determine_winner(state, columns, rows)


if __name__ == "__main__":
    play_game("expectiminimax", 3, 7, 6)
