def heuristic(board):
    score = 0
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