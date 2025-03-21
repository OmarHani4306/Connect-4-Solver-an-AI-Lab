from helpers import *
from utils import ROWS, COLS, print_tree

def expectiminimax(state, depth, maximizing_player,node_type, max_depth):
    
    if is_terminal(state, depth, max_depth):
        value = heuristic(state)  
        # if print_tree:
        #     print(f"{'|   ' * depth}Leaf Node: Heuristic={value}")
        return value, None, {'type': 'leaf', 'value': value, 'move': None, 'children': []}

    # Create a node for the tree
    tree = {'type': node_type, 'value': None, 'move': None, 'children': []}

    if node_type == 'max':
        max_eval = -float('inf')
        best_move = None
        # print(print_board(string_to_board(state, ROWS, COLS)))

        for column in valid_moves(state, COLS, ROWS):  
            # Simulate AI move
            new_state = apply_move(state, column, 1, COLS, ROWS)
            eval, _, child_tree = expectiminimax(new_state, depth + 1,False ,'chance', max_depth)

            if eval > max_eval:
                max_eval = eval
                best_move = column

            # Add this chance node as a child to the Max Node
            tree['children'].append({'type': 'chance', 'value': eval, 'move': column, 'children': child_tree['children']})

        tree['value'] = max_eval
        tree['move'] = best_move
        return max_eval, best_move, tree

    elif node_type == 'min':
        min_eval = float('inf')
        best_move = None

        for column in valid_moves(state, COLS, ROWS):  
            # Simulate Human move
            new_state = apply_move(state, column, 2, COLS, ROWS)
            eval, _, child_tree = expectiminimax(new_state, depth + 1, True,'chance', max_depth)

            if eval < min_eval:
                min_eval = eval
                best_move = column

            tree['children'].append({'type': 'chance', 'value': eval, 'move': column, 'children': child_tree['children']})

        tree['value'] = min_eval
        tree['move'] = best_move
        return min_eval, best_move, tree

    elif node_type == 'chance':
        expected_value = 0
        chance_children = []

        valid_moves_cols = valid_moves(state, COLS, ROWS)

        for column in valid_moves_cols:  # Simulate dropping into current, left, and right COLS
            # Center column
            center_state = apply_move(state, column, 1 if maximizing_player else 2, COLS, ROWS)
            center_eval, _, center_tree = expectiminimax(center_state, depth + 1,not maximizing_player ,'min' if not maximizing_player else 'max', max_depth)

            # Left neighbor
            left_eval = 0
            if column > 0 and column-1 in valid_moves_cols:

                left_state = apply_move(state, column - 1, 1 if maximizing_player else 2, COLS, ROWS)
                left_eval, _, _ = expectiminimax(left_state, depth + 1, not maximizing_player ,'min' if not maximizing_player else 'max', max_depth)

            # Right neighbor
            right_eval = 0
            if column < COLS - 1 and column+1 in valid_moves_cols:
                right_state = apply_move(state, column + 1, 1 if maximizing_player else 2, COLS, ROWS)
                right_eval, _, _ = expectiminimax(right_state, depth + 1, not maximizing_player ,'min' if not maximizing_player else 'max', max_depth)

            
            if column == 0:  # First column
                expected_value += 0.6 * center_eval + 0.4 * right_eval
            elif column == COLS - 1:  # Last column
                expected_value += 0.6 * center_eval + 0.4 * left_eval
            else:  # Middle COLS
                expected_value += 0.6 * center_eval + 0.2 * left_eval + 0.2 * right_eval

            
            chance_children.append({'type': 'min' if not maximizing_player else 'max', 'value': center_eval, 'move': column, 'children': center_tree['children']})

        tree['value'] = expected_value
        tree['children'] = chance_children
        return expected_value, None, tree
