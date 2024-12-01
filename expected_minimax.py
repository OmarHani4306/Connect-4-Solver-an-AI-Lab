from helpers import valid_moves, apply_move, is_terminal, heuristic

def expectiminimax(state, depth, node_type, max_depth, columns, rows, print_tree=True):
    
    if is_terminal(state, depth, max_depth):
        value = heuristic(state, columns, rows)  
        if print_tree:
            print(f"{'|   ' * depth}Leaf Node: Heuristic={value}")
        return value, None, {'type': 'leaf', 'value': value, 'move': None, 'children': []}

    # Create a node for the tree
    tree = {'type': node_type, 'value': None, 'move': None, 'children': []}

    if node_type == 'max':
        max_eval = -float('inf')
        best_move = None

        for column in valid_moves(state, columns, rows):  
            # Simulate AI move
            new_state = apply_move(state, column, 1, columns, rows)
            eval, _, child_tree = expectiminimax(new_state, depth + 1, 'chance', max_depth, columns, rows, print_tree)

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

        for column in valid_moves(state, columns, rows):  
            # Simulate Human move
            new_state = apply_move(state, column, 2, columns, rows)
            eval, _, child_tree = expectiminimax(new_state, depth + 1, 'chance', max_depth, columns, rows, print_tree)

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

        for column in valid_moves(state, columns, rows):  # Simulate dropping into current, left, and right columns
            # Center column
            center_state = apply_move(state, column, 1 if depth % 2 == 0 else 2, columns, rows)
            center_eval, _, center_tree = expectiminimax(center_state, depth + 1, 'min' if depth % 2 == 0 else 'max', max_depth, columns, rows, print_tree)

            # Left neighbor
            left_eval = 0
            if column > 0:
                left_state = apply_move(state, column - 1, 1 if depth % 2 == 0 else 2, columns, rows)
                left_eval, _, _ = expectiminimax(left_state, depth + 1, 'min' if depth % 2 == 0 else 'max', max_depth, columns, rows, print_tree)

            # Right neighbor
            right_eval = 0
            if column < columns - 1:
                right_state = apply_move(state, column + 1, 1 if depth % 2 == 0 else 2, columns, rows)
                right_eval, _, _ = expectiminimax(right_state, depth + 1, 'min' if depth % 2 == 0 else 'max', max_depth, columns, rows, print_tree)

            
            if column == 0:  # First column
                expected_value += 0.6 * center_eval + 0.4 * right_eval
            elif column == columns - 1:  # Last column
                expected_value += 0.6 * center_eval + 0.4 * left_eval
            else:  # Middle columns
                expected_value += 0.6 * center_eval + 0.2 * left_eval + 0.2 * right_eval

            
            chance_children.append({'type': 'min' if depth % 2 == 0 else 'max', 'value': center_eval, 'move': column, 'children': center_tree['children']})

        tree['value'] = expected_value
        tree['children'] = chance_children
        return expected_value, None, tree
