from helpers import valid_moves, apply_move, is_terminal, heuristic 
# state is integer
from utils import *

memo = {}

def minimax(state, depth, maximizingPlayer):
    global MAX_DEPTH
    # print(MAX_DEPTH)
    if (state, maximizingPlayer) in memo:
        return memo[(state, maximizingPlayer)]
    
    if is_terminal(state, depth, MAX_DEPTH):

        value = heuristic(str(state).zfill(ROWS*COLS))  # change
        return value, None, {'type': 'leaf', 'value': value, 'move': None, 'children': []}

    tree = {'type': 'max' if maximizingPlayer else 'min', 'value': None, 'move': None, 'children': []}

    if maximizingPlayer:
        max_eval = -float('inf')
        best_move = None

        for column in valid_moves(state):  # Pass rows and columns
            new_state = apply_move(state, column, 1)  # Pass rows and columns
            eval, _, child_tree = minimax(new_state, depth + 1, False)

            if eval > max_eval:
                max_eval = eval
                best_move = column

            tree['children'].append({'type': 'min', 'value': eval, 'move': column, 'children': child_tree['children']})

        tree['value'] = max_eval
        tree['move'] = best_move
        memo[(state, maximizingPlayer)] = max_eval, best_move, tree
        return max_eval, best_move, tree
        # return max_eval, best_move, 0

    else:
        min_eval = float('inf')
        best_move = None

        for column in valid_moves(state):  # Pass rows and columns
            new_state = apply_move(state, column, 2)  # Pass rows and columns
            eval, _, child_tree = minimax(new_state, depth + 1, True)

            if eval < min_eval:
                min_eval = eval
                best_move = column

            tree['children'].append({'type': 'max', 'value': eval, 'move': column, 'children': child_tree['children']})

        tree['value'] = min_eval
        tree['move'] = best_move
        memo[(state, maximizingPlayer)] = min_eval, best_move, tree
        return min_eval, best_move, tree
        # return min_eval, best_move, 0

import time

def main():
    # Define constants
    global ROWS, COLS, MAX_DEPTH
    ROWS, COLS = 6, 7  # Example for a Connect Four board
    MAX_DEPTH = 8  # Define how deep the minimax algorithm will explore

    # Example initial state and depth configuration
    initial_state = 0  # Representing the empty board as an integer
    maximizing_player = True  # Start with the maximizing player

    # Start the timer
    start_time = time.time()

    # Test minimax
    score, best_move, tree_info = minimax(initial_state, depth=0, maximizingPlayer=maximizing_player)

    # End the timer
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    print("Best Score:", score)
    print("Best Move:", best_move)
    # print("Tree Info:", tree_info)
    print(f"Execution Time: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    main()