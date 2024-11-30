from heuristic.py import heuristic

def expected_minimax(state, depth, maximizingPlayer, max_depth, print_tree=True):
    
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
            center_state = apply_move(state, column, 1)
            center_eval, _, child_tree = expected_minimax(center_state, depth + 1, False, max_depth, print_tree)
            
            left_eval = 0
            right_eval = 0

            if column == 0:  
                right_state = apply_move(state, column + 1, 1)
                right_eval, _, _ = expected_minimax(right_state, depth + 1, False, max_depth, print_tree)
                expected_value = 0.6 * center_eval + 0.4 * right_eval  

            elif column == 6:  
                left_state = apply_move(state, column - 1, 1)
                left_eval, _, _ = expected_minimax(left_state, depth + 1, False, max_depth, print_tree)
                expected_value = 0.6 * center_eval + 0.4 * left_eval  

            else:  
                left_state = apply_move(state, column - 1, 1)
                left_eval, _, _ = expected_minimax(left_state, depth + 1, False, max_depth, print_tree)

                right_state = apply_move(state, column + 1, 1)
                right_eval, _, _ = expected_minimax(right_state, depth + 1, False, max_depth, print_tree)

                expected_value = 0.6 * center_eval + 0.2 * left_eval + 0.2 * right_eval
           
            if expected_value > max_eval:
                max_eval = expected_value
                best_move = column

            tree['children'].append({'value': expected_value, 'move': column, 'children': child_tree['children']})

        tree['value'] = max_eval
        tree['move'] = best_move
        return max_eval, best_move, tree

    else:
        min_eval = float('inf')
        best_move = None

        for column in valid_moves(state):
            
            center_state = apply_move(state, column, 2)
            center_eval, _, child_tree = expected_minimax(center_state, depth + 1, True, max_depth, print_tree)
            
            left_eval = 0
            right_eval = 0

            
            if column == 0:  
                right_state = apply_move(state, column + 1, 2)
                right_eval, _, _ = expected_minimax(right_state, depth + 1, True, max_depth, print_tree)
                expected_value = 0.6 * center_eval + 0.4 * right_eval  

            elif column == 6:  
                left_state = apply_move(state, column - 1, 2)
                left_eval, _, _ = expected_minimax(left_state, depth + 1, True, max_depth, print_tree)
                expected_value = 0.6 * center_eval + 0.4 * left_eval 

            else:  
                left_state = apply_move(state, column - 1, 2)
                left_eval, _, _ = expected_minimax(left_state, depth + 1, True, max_depth, print_tree)

                right_state = apply_move(state, column + 1, 2)
                right_eval, _, _ = expected_minimax(right_state, depth + 1, True, max_depth, print_tree)

                expected_value = 0.6 * center_eval + 0.2 * left_eval + 0.2 * right_eval

            if expected_value < min_eval:
                min_eval = expected_value
                best_move = column

            
            tree['children'].append({'value': expected_value, 'move': column, 'children': child_tree['children']})

        tree['value'] = min_eval
        tree['move'] = best_move
        return min_eval, best_move, tree

