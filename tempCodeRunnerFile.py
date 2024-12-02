def valid_moves(state):
    valid = []
    for col in range(41,34,-1):
        if (state // (10 ** col)) % 10 == 0:
            valid.append(42 - col - 1)
    return valid
