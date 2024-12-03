from utils import *

def heuristic(board):
    score = 0
    # print(board)
    for i in range(6):
        for j in range(7):
            if board[i * 7 + j] == "0":
                if (
                    i + 3 <= 5 and j + 3 <= 6 and
                    (
                        (board[(i + 1) * 7 + j + 1] == "1" and board[(i + 2) * 7 + j + 2] == "0" and board[(i + 3) * 7 + j + 3] == "1") or
                        (board[(i + 1) * 7 + j + 1] == "0" and board[(i + 2) * 7 + j + 2] == "1" and board[(i + 3) * 7 + j + 3] == "1") or
                        (board[(i + 1) * 7 + j + 1] == "1" and board[(i + 2) * 7 + j + 2] == "1" and board[(i + 3) * 7 + j + 3] == "0")
                    )
                ):
                    score += 400000

                if (
                    i - 3 >= 0 and j + 3 <= 6 and
                    (
                        (board[(i - 1) * 7 + j + 1] == "1" and board[(i - 2) * 7 + j + 2] == "0" and board[(i - 3) * 7 + j + 3] == "1") or
                        (board[(i - 1) * 7 + j + 1] == "0" and board[(i - 2) * 7 + j + 2] == "1" and board[(i - 3) * 7 + j + 3] == "1") or
                        (board[(i - 1) * 7 + j + 1] == "1" and board[(i - 2) * 7 + j + 2] == "1" and board[(i - 3) * 7 + j + 3] == "0")
                    )
                ):
                    score += 400000

                if i + 3 <= 5 and j + 3 <= 6 and (
                    board[(i + 1) * 7 + j + 1] == "1" and
                    board[(i + 2) * 7 + j + 2] == "1" and
                    board[(i + 3) * 7 + j + 3] == "1"
                ):
                    score += 3000000

                if i - 3 >= 0 and j + 3 <= 6 and (
                    board[(i - 1) * 7 + j + 1] == "1" and
                    board[(i - 2) * 7 + j + 2] == "1" and
                    board[(i - 3) * 7 + j + 3] == "1"
                ):
                    score += 3000000


            if board[i * 7 + j] == "1":
                score += [200, 100, 75, 50][abs(j - 3)]

                left_adjacent, right_adjacent = 0, 0
                if j + 1 <= 6 and board[i * 7 + j + 1] == "1":
                    temp = j
                    while j - 1 >= 0 and board[i * 7 + j - 1] == "0":
                        left_adjacent += 1
                        j -= 1
                    j = temp + 1
                    while j + 1 <= 6 and board[i * 7 + j + 1] == "0":
                        right_adjacent += 1
                        j += 1
                    if left_adjacent and right_adjacent or left_adjacent >= 2 or right_adjacent >= 2:
                        score += 100000 * (left_adjacent + right_adjacent)
                    j = temp

                if i + 3 <= 5 and j + 3 <= 6 and (
                    board[(i + 1) * 7 + j + 1] == "1" and
                    board[(i + 2) * 7 + j + 2] == "0" and
                    board[(i + 3) * 7 + j + 3] == "0"
                ):
                    score += 400000

                if i - 3 >= 0 and j + 3 <= 6 and (
                    board[(i - 1) * 7 + j + 1] == "1" and
                    board[(i - 2) * 7 + j + 2] == "0" and
                    board[(i - 3) * 7 + j + 3] == "0"
                ):
                    score += 400000

                if i - 3 >= 0 and (
                    board[(i - 1) * 7 + j] == "1" and
                    board[(i - 2) * 7 + j] == "0" and
                    board[(i - 3) * 7 + j] == "0"
                ):
                    score += 400000

                if (
                    j + 2 <= 6 and
                    board[i * 7 + j + 1] == "1" and
                    board[i * 7 + j + 2] == "1"
                ):
                    if (
                        j - 1 >= 0 and j + 3 <= 6 and
                        board[i * 7 + j - 1] != "0" and
                        board[i * 7 + j + 3] != "0"
                    ):
                        score += 0
                    elif (
                        j - 1 >= 0 and j + 3 <= 6 and
                        board[i * 7 + j - 1] == "0" and
                        board[i * 7 + j + 3] == "0" and
                        (i == 5 or (
                            board[(i + 1) * 7 + j - 1] != "0" and
                            board[(i + 1) * 7 + j + 3] != "0"
                        ))
                    ):
                        score += 100000000
                    else:
                        left_adjacent, right_adjacent = 0, 0
                        temp = j
                        while j - 1 >= 0 and board[i * 7 + j - 1] == "0":
                            left_adjacent += 1
                            j -= 1
                        j = temp + 2
                        while j + 1 <= 6 and board[i * 7 + j + 1] == "0":
                            right_adjacent += 1
                            j += 1
                        score += 1000000 * (left_adjacent + right_adjacent)
                        j = temp

                if i - 3 >= 0 and board[(i - 1) * 7 + j] == "1" and board[(i - 2) * 7 + j] == "1" and board[(i - 3) * 7 + j] == "0":
                    score += 3000000

                if i - 3 >= 0 and board[(i - 1) * 7 + j] == "1" and board[(i - 2) * 7 + j] == "1" and board[(i - 3) * 7 + j] == "1":
                    score += 100000000

                if i - 3 >= 0 and j + 3 <= 6 and board[(i - 1) * 7 + j + 1] == "1" and board[(i - 2) * 7 + j + 2] == "1" and board[(i - 3) * 7 + j + 3] == "0":
                    score += 3000000

                if i - 3 >= 0 and j + 3 <= 6 and board[(i - 1) * 7 + j + 1] == "1" and board[(i - 2) * 7 + j + 2] == "1" and board[(i - 3) * 7 + j + 3] == "1":
                    score += 100000000

                if i + 3 <= 5 and j + 3 <= 6 and board[(i + 1) * 7 + j + 1] == "1" and board[(i + 2) * 7 + j + 2] == "1" and board[(i + 3) * 7 + j + 3] == "0":
                    score += 3000000

                if i + 3 <= 5 and j + 3 <= 6 and board[(i + 1) * 7 + j + 1] == "1" and board[(i + 2) * 7 + j + 2] == "1" and board[(i + 3) * 7 + j + 3] == "1":
                    score += 100000000

                if j + 3 <= 6 and board[i * 7 + j + 1] == "1" and board[i * 7 + j + 2] == "1" and board[i * 7 + j + 3] == "1":
                    score += 100000000

                if j + 3 <= 6 and (
                    (board[i * 7 + j + 1] == "1" and board[i * 7 + j + 2] == "0" and board[i * 7 + j + 3] == "1") or
                    (board[i * 7 + j + 1] == "0" and board[i * 7 + j + 2] == "1" and board[i * 7 + j + 3] == "1")
                ):
                    score += 3000000

                if i - 3 >= 0 and j + 3 <= 6 and (
                    (board[(i - 1) * 7 + j + 1] == "1" and board[(i - 2) * 7 + j + 2] == "0" and board[(i - 3) * 7 + j + 3] == "1") or
                    (board[(i - 1) * 7 + j + 1] == "0" and board[(i - 2) * 7 + j + 2] == "1" and board[(i - 3) * 7 + j + 3] == "1")
                ):
                    score += 3000000

                if i + 3 <= 5 and j + 3 <= 6 and (
                    (board[(i + 1) * 7 + j + 1] == "1" and board[(i + 2) * 7 + j + 2] == "0" and board[(i + 3) * 7 + j + 3] == "1") or
                    (board[(i + 1) * 7 + j + 1] == "0" and board[(i + 2) * 7 + j + 2] == "1" and board[(i + 3) * 7 + j + 3] == "1")
                ):
                    score += 3000000

                if j + 3 <= 6 and (
                    (board[i * 7 + j + 1] == "0" and board[i * 7 + j + 2] == "1" and board[i * 7 + j + 3] == "0") or
                    (board[i * 7 + j + 1] == "0" and board[i * 7 + j + 2] == "0" and board[i * 7 + j + 3] == "1")
                ):
                    score += 400000

                if i - 3 >= 0 and j + 3 <= 6 and (
                    (board[(i - 1) * 7 + j + 1] == "0" and board[(i - 2) * 7 + j + 2] == "1" and board[(i - 3) * 7 + j + 3] == "0") or
                    (board[(i - 1) * 7 + j + 1] == "0" and board[(i - 2) * 7 + j + 2] == "0" and board[(i - 3) * 7 + j + 3] == "1")
                ):
                    score += 400000

                if i + 3 <= 5 and j + 3 <= 6 and (
                    (board[(i + 1) * 7 + j + 1] == "0" and board[(i + 2) * 7 + j + 2] == "1" and board[(i + 3) * 7 + j + 3] == "0") or
                    (board[(i + 1) * 7 + j + 1] == "0" and board[(i + 2) * 7 + j + 2] == "0" and board[(i + 3) * 7 + j + 3] == "1")
                ):
                    score += 400000

                if j + 3 <= 6 and board[i * 7 + j + 1] == "2" and board[i * 7 + j + 2] == "2" and board[i * 7 + j + 3] == "2":
                    score += 50000000

                if i - 3 >= 0 and board[(i - 1) * 7 + j] == "2" and board[(i - 2) * 7 + j] == "2" and board[(i - 3) * 7 + j] == "2":
                    score += 50000000

                if i - 3 >= 0 and j + 3 <= 6 and board[(i - 1) * 7 + j + 1] == "2" and board[(i - 2) * 7 + j + 2] == "2" and board[(i - 3) * 7 + j + 3] == "2":
                    score += 50000000

                if i + 3 <= 5 and j + 3 <= 6 and board[(i + 1) * 7 + j + 1] == "2" and board[(i + 2) * 7 + j + 2] == "2" and board[(i + 3) * 7 + j + 3] == "2":
                    score += 50000000

            if board[i * 7 + j] == "2":
                if (
                    j + 3 <= 6 and (
                        (board[i * 7 + j + 1] == "2" and board[i * 7 + j + 2] == "2" and board[i * 7 + j + 3] == "1") or
                        (board[i * 7 + j + 1] == "2" and board[i * 7 + j + 2] == "1" and board[i * 7 + j + 3] == "2") or
                        (board[i * 7 + j + 1] == "1" and board[i * 7 + j + 2] == "2" and board[i * 7 + j + 3] == "2")
                    )
                ):
                    score += 50000000

                if i - 3 >= 0 and board[(i - 1) * 7 + j] == "2" and board[(i - 2) * 7 + j] == "2" and board[(i - 3) * 7 + j] == "1":
                    score += 50000000

                if (
                    i - 3 >= 0 and j + 3 <= 6 and (
                        (board[(i - 1) * 7 + j + 1] == "2" and board[(i - 2) * 7 + j + 2] == "2" and board[(i - 3) * 7 + j + 3] == "1") or
                        (board[(i - 1) * 7 + j + 1] == "2" and board[(i - 2) * 7 + j + 2] == "1" and board[(i - 3) * 7 + j + 3] == "2") or
                        (board[(i - 1) * 7 + j + 1] == "1" and board[(i - 2) * 7 + j + 2] == "2" and board[(i - 3) * 7 + j + 3] == "2")
                    )
                ):
                    score += 50000000

                if (
                    i + 3 <= 5 and j + 3 <= 6 and (
                        (board[(i + 1) * 7 + j + 1] == "2" and board[(i + 2) * 7 + j + 2] == "2" and board[(i + 3) * 7 + j + 3] == "1") or
                        (board[(i + 1) * 7 + j + 1] == "2" and board[(i + 2) * 7 + j + 2] == "1" and board[(i + 3) * 7 + j + 3] == "2") or
                        (board[(i + 1) * 7 + j + 1] == "1" and board[(i + 2) * 7 + j + 2] == "2" and board[(i + 3) * 7 + j + 3] == "2")
                    )
                ):
                    score += 50000000

                if (
                    j + 2 <= 6 and (
                        (board[i * 7 + j + 1] == "2" and board[i * 7 + j + 2] == "1") or
                        (board[i * 7 + j + 1] == "1" and board[i * 7 + j + 2] == "2")
                    )
                ):
                    score += 200000

                if (
                    i - 2 >= 0 and (
                        (board[(i - 1) * 7 + j] == "2" and board[(i - 2) * 7 + j] == "1") or
                        (board[(i - 1) * 7 + j] == "1" and board[(i - 2) * 7 + j] == "2")
                    )
                ):
                    score += 200000

                if (
                    i - 2 >= 0 and j + 2 <= 6 and (
                        (board[(i - 1) * 7 + j + 1] == "2" and board[(i - 2) * 7 + j + 2] == "1") or
                        (board[(i - 1) * 7 + j + 1] == "1" and board[(i - 2) * 7 + j + 2] == "2")
                    )
                ):
                    score += 200000

                if (
                    i + 2 <= 5 and j + 2 <= 6 and (
                        (board[(i + 1) * 7 + j + 1] == "2" and board[(i + 2) * 7 + j + 2] == "1") or
                        (board[(i + 1) * 7 + j + 1] == "1" and board[(i + 2) * 7 + j + 2] == "2")
                    )
                ):
                    score += 200000

    return score

def board_to_string(board):
    return ''.join([str(cell) for row in board for cell in row])

# change
# def valid_moves(state):
#     valid = []
#     for col in range(COLS):
#         index = (ROWS - 1) * COLS + col
#         if (state // (10 ** index)) % 10 == 0:
#             valid.append(COLS - col - 1)
#     return valid


def valid_moves(state):
    valid = []
    for col in range(41,34,-1):
        if (state // (10 ** col)) % 10 == 0:
            valid.append(42 - col - 1)
    return valid

#change
def apply_move(state, column, player):
    for row in range(ROWS):
        index = row*COLS + (COLS - column -1)
        if (state // (10 ** index)) % 10 == 0:
            return state + (player * (10 ** index))
    raise ValueError(f"Column {column} is full.")


#change
def is_terminal(state, depth, max_depth):
    return depth >= max_depth or len(valid_moves(state)) == 0 
   

#change
def count_connected_fours(state, player):
    def get_cell(state, row, col):
        position = (ROWS - 1 - row) * COLS + col
        return (state // (3 ** position)) % 3  

    count = 0

    # Horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):  # Check up to column - 3
            if all(get_cell(state, row, col + i) == player for i in range(4)):
                count += 1

    # Vertical
    for col in range(COLS):
        for row in range(ROWS - 3):  # Check up to row - 3
            if all(get_cell(state, row + i, col) == player for i in range(4)):
                count += 1

    # Diagonal (Bottom-Left to Top-Right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(get_cell(state, row + i, col + i) == player for i in range(4)):
                count += 1

    # Diagonal (Bottom-Right to Top-Left)
    for row in range(ROWS - 3):
        for col in range(3, COLS):
            if all(get_cell(state, row + i, col - i) == player for i in range(4)):
                count += 1

    return count


def determine_winner(state):
   
    ai_score = count_connected_fours(state, 1)
    human_score = count_connected_fours(state, 2)

    print("Game Over!")
    if ai_score > human_score:
        print(f"AI Wins! AI: {ai_score}, Human: {human_score}")
    elif human_score > ai_score:
        print(f"You Win! AI: {ai_score}, Human: {human_score}")
    else:
        print(f"It's a Draw! AI: {ai_score}, Human: {human_score}")
