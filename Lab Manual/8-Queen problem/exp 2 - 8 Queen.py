N = 8

board = [[0] * N for _ in range(N)]

def is_safe(row, col):
    for i in range(col):
        if board[row][i]:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True

def solve(col):
    if col >= N:
        return True

    for row in range(N):
        if is_safe(row, col):
            board[row][col] = 1

            if solve(col + 1):
                return True

            board[row][col] = 0

    return False

if solve(0):
    print("Solution:")
    for row in board:
        print(*row)
else:
    print("No solution exists")
