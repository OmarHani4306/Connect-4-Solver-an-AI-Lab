from helpers import valid_moves, apply_move, is_terminal, heuristic
from utils import *

memo = {}

def expectiminimax(state, depth, maximizing_player,node_type):

    if (state, node_type) in memo:
        return memo[(state, node_type)]

    if is_terminal(state, depth, MAX_DEPTH):
        
        value = heuristic(str(state).zfill(42))  
        # if print_tree:
        #     print(f"{'|   ' * depth}Leaf Node: Heuristic={value}")
        return value, None, {'type': 'leaf', 'value': value, 'move': None, 'children': []}

    # Create a node for the tree
    tree = {'type': node_type, 'value': None, 'move': None, 'children': []}

    if node_type == 'max':
        max_eval = -float('inf')
        best_move = None
        # print(print_board(string_to_board(state, rows, columns)))

        for column in valid_moves(state): 
            # Simulate AI move
            new_state = apply_move(state, column, 1)
            eval, _, child_tree = expectiminimax(new_state, depth + 1,False ,'chance')

            if eval > max_eval:
                max_eval = eval
                best_move = column

            # Add this chance node as a child to the Max Node
            tree['children'].append({'type': 'chance', 'value': eval, 'move': column, 'children': child_tree['children']})

        tree['value'] = max_eval
        tree['move'] = best_move
        memo[(state, node_type)] = max_eval, best_move, tree
        return max_eval, best_move, tree

    elif node_type == 'min':
        min_eval = float('inf')
        best_move = None

        for column in valid_moves(state):  
            # Simulate Human move
            new_state = apply_move(state, column, 2)
            eval, _, child_tree = expectiminimax(new_state, depth + 1, True,'chance')

            if eval < min_eval:
                min_eval = eval
                best_move = column

            tree['children'].append({'type': 'chance', 'value': eval, 'move': column, 'children': child_tree['children']})

        tree['value'] = min_eval
        tree['move'] = best_move
        memo[(state, node_type)] = min_eval, best_move, tree
        return min_eval, best_move, tree

    elif node_type == 'chance':
        expected_value = 0
        chance_children = []

        valid_moves_columns = valid_moves(state)

        for column in valid_moves_columns:  # Simulate dropping into current, left, and right columns
            # Center column
            center_state = apply_move(state, column, 1 if maximizing_player else 2)
            center_eval, _, center_tree = expectiminimax(center_state, depth + 1,not maximizing_player ,'min' if not maximizing_player else 'max')

            # Left neighbor
            left_eval = 0
            if column > 0 and column-1 in valid_moves_columns:

                left_state = apply_move(state, column - 1, 1 if maximizing_player else 2)
                left_eval, _, _ = expectiminimax(left_state, depth + 1, not maximizing_player ,'min' if not maximizing_player else 'max')

            # Right neighbor
            right_eval = 0
            if column < COLS - 1 and column+1 in valid_moves_columns:
                right_state = apply_move(state, column + 1, 1 if maximizing_player else 2)
                right_eval, _, _ = expectiminimax(right_state, depth + 1, not maximizing_player ,'min' if not maximizing_player else 'max')

            
            if column == 0:  # First column
                expected_value += 0.6 * center_eval + 0.4 * right_eval
            elif column == COLS - 1:  # Last column
                expected_value += 0.6 * center_eval + 0.4 * left_eval
            else:  # Middle columns
                expected_value += 0.6 * center_eval + 0.2 * left_eval + 0.2 * right_eval

            
            chance_children.append({'type': 'min' if not maximizing_player else 'max', 'value': center_eval, 'move': column, 'children': center_tree['children']})

        tree['value'] = expected_value
        tree['children'] = chance_children
        memo[(state, node_type)] = expected_value, None, tree
        return expected_value, None, tree
    
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
    score, best_move, tree_info = expectiminimax(initial_state, 0, maximizing_player, 'max')

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