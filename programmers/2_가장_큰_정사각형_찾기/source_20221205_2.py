def solution(board):
    answer = 0
    row_size = len(board)
    col_size = len(board[0])
    if row_size == 1 and col_size == 1:
        return board[0][0]
    
    for r in range(row_size):
        for c in range(col_size):
            if r-1 < 0 : continue
            if c-1 < 0 : continue
            if board[r-1][c] == 0 or board[r][c-1] == 0 or board[r][c] == 0 : continue

            if board[r-1][c] == board[r][c-1] and board[r-1][c]==board[r-1][c-1]:
                board[r][c] = board[r-1][c] + 1
            else:
                board[r][c] = min(board[r-1][c], board[r][c-1], board[r-1][c-1]) + 1
            answer = max(answer, board[r][c])
    return answer**2
