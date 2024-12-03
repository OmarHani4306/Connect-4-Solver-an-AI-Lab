from helpers import valid_moves, apply_move, is_terminal, heuristic
from utils import ROWS, COLS, MAX_DEPTH

memo = {}
no_of_nodes = 0

def alphabeta_minimax(state, depth, alpha, beta, maximizingPlayer, max_depth):
    # print(state)
    # print(max_depth)
    global no_of_nodes
    if (state, maximizingPlayer) in memo:
        return memo[(state, maximizingPlayer)]

    if is_terminal(state, depth, max_depth):
        value = heuristic(str(state).zfill(ROWS*COLS))  
        return value, None, {'type': 'leaf', 'value': value, 'move': None, 'children': []}

    tree = {'type': 'max' if maximizingPlayer else 'min', 'value': None, 'move': None, 'children': []}

    if maximizingPlayer:
        max_eval = -float('inf')
        best_move = None

        for column in valid_moves(state):  
            new_state = apply_move(state, column, 1)  
            eval, _, child_tree = alphabeta_minimax(new_state, depth + 1, alpha, beta, False, max_depth)

            if eval > max_eval:
                max_eval = eval
                best_move = column

            alpha = max(alpha, eval)
            if alpha >= beta:  # Pruning
                break

            tree['children'].append({'type': 'min', 'value': eval, 'move': column, 'children': child_tree['children']})
        no_of_nodes += 1
        tree['value'] = max_eval
        tree['move'] = best_move
        memo[(state, maximizingPlayer)] = max_eval, best_move, tree
        return max_eval, best_move, tree

    else:
        min_eval = float('inf')
        best_move = None

        for column in valid_moves(state):  
            new_state = apply_move(state, column, 2)  
            eval, _, child_tree = alphabeta_minimax(new_state, depth + 1, alpha, beta, True, max_depth)

            if eval < min_eval:
                min_eval = eval
                best_move = column

            beta = min(beta, eval)
            if alpha >= beta:  # Pruning
                break

            tree['children'].append({'type': 'max', 'value': eval, 'move': column, 'children': child_tree['children']})
        no_of_nodes += 1
        tree['value'] = min_eval
        tree['move'] = best_move
        memo[(state, maximizingPlayer)] = min_eval, best_move, tree
        return min_eval, best_move, tree
    
import time
def fn():
    print(MAX_DEPTH)
def main():
    # Define constants
    global ROWS, COLS, MAX_DEPTH
    ROWS, COLS = 6, 7  # Example for a Connect Four board
    max_depth = 12  # Define how deep the minimax algorithm will explore

    # Example initial state and depth configuration
    initial_state = 0  # Representing the empty board as an integer
    maximizing_player = True  # Start with the maximizing player

    # Start the timer
    start_time = time.time()

    # Test minimax
    score, best_move, tree_info = alphabeta_minimax(initial_state, 0, -float('inf'), float('inf') , maximizing_player, max_depth)

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