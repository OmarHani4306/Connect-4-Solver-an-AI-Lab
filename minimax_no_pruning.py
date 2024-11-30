from heuristic.py import heuristic
def minimax(state, depth, maximizingPlayer, max_depth, print_tree=True):
   
    if depth >= max_depth or is_terminal(state, depth, max_depth):
        value = heuristic(state)
        if print_tree:
            print(f"{'|   ' * depth}Leaf Node: Heuristic={value}")
        return value, None, {'value': value, 'move': None, 'children': []}

    tree = {'value': None, 'move': None, 'children': []}

    if maximizingPlayer:
        max_eval = -float('inf')
        best_move = None

        for column in valid_moves(state):
            new_state = apply_move(state, column, 1)  # AI
            eval, _, child_tree = minimax(new_state, depth + 1, False, max_depth, print_tree)

            if eval > max_eval:
                max_eval = eval
                best_move = column

            tree['children'].append({'value': eval, 'move': column, 'children': child_tree['children']})

        tree['value'] = max_eval
        tree['move'] = best_move
        return max_eval, best_move, tree

    else:
        min_eval = float('inf')
        best_move = None

        for column in valid_moves(state):
            new_state = apply_move(state, column, 2)  # Human
            eval, _, child_tree = minimax(new_state, depth + 1, True, max_depth, print_tree)

            if eval < min_eval:
                min_eval = eval
                best_move = column

            tree['children'].append({'value': eval, 'move': column, 'children': child_tree['children']})

        tree['value'] = min_eval
        tree['move'] = best_move
        return min_eval, best_move, tree
