from helpers import valid_moves, apply_move, is_terminal, heuristic

def minimax(state, depth, maximizingPlayer, max_depth, columns, rows, print_tree=True):
    
    if is_terminal(state, depth, max_depth):
        value = heuristic(state, columns, rows)  # Implement your heuristic here
        return value, None, {'type': 'leaf', 'value': value, 'move': None, 'children': []}

    tree = {'type': 'max' if maximizingPlayer else 'min', 'value': None, 'move': None, 'children': []}

    if maximizingPlayer:
        max_eval = -float('inf')
        best_move = None

        for column in valid_moves(state, columns, rows):  # Pass rows and columns
            new_state = apply_move(state, column, 1, columns, rows)  # Pass rows and columns
            eval, _, child_tree = minimax(new_state, depth + 1, False, max_depth, columns, rows, print_tree)

            if eval > max_eval:
                max_eval = eval
                best_move = column

            tree['children'].append({'type': 'min', 'value': eval, 'move': column, 'children': child_tree['children']})

        tree['value'] = max_eval
        tree['move'] = best_move
        return max_eval, best_move, tree

    else:
        min_eval = float('inf')
        best_move = None

        for column in valid_moves(state, columns, rows):  # Pass rows and columns
            new_state = apply_move(state, column, 2, columns, rows)  # Pass rows and columns
            eval, _, child_tree = minimax(new_state, depth + 1, True, max_depth, columns, rows, print_tree)

            if eval < min_eval:
                min_eval = eval
                best_move = column

            tree['children'].append({'type': 'max', 'value': eval, 'move': column, 'children': child_tree['children']})

        tree['value'] = min_eval
        tree['move'] = best_move
        return min_eval, best_move, tree
