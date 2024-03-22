def is_valid(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == board[0][0] ^ (i + j) % 2:
                continue
            else:
                return False
    return True

def count_deviation(board):
    n = len(board)
    deviation_rows = deviation_cols = 0
    for i in range(n):
        row = board[i]
        col = [board[j][i] for j in range(n)]
        if row.count(0) != n // 2 or row.count(1) != n // 2:
            deviation_rows += 1
        if col.count(0) != n // 2 or col.count(1) != n // 2:
            deviation_cols += 1
    return deviation_rows, deviation_cols

def min_swaps_to_chessboard(board):
    n = len(board)
    deviation_rows, deviation_cols = count_deviation(board)
    if deviation_rows != 0 and deviation_rows != 2:
        return -1
    if deviation_cols != 0 and deviation_cols != 2:
        return -1
    
    if deviation_rows == 2:
        for i in range(n):
            for j in range(i + 1, n):
                board[i], board[j] = board[j], board[i]
                if is_valid(board):
                    return (j - i) // 2
                board[i], board[j] = board[j], board[i]
    else: 
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(n):
                    board[k][i], board[k][j] = board[k][j], board[k][i]
                if is_valid(board):
                    return (j - i) // 2
                for k in range(n):
                    board[k][i], board[k][j] = board[k][j], board[k][i]
    return -1


board = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]
print(min_swaps_to_chessboard(board)) 
