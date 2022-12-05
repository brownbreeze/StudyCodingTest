def isrectangle(board, fr,fc,l):
    for r in range(fr, fr+l):
        for c in range(fc, fc+l):
            if board[r][c] == 0:
                return False
    return True
    
def solution(board):
    answer = 1
    max_len = len(board) if len(board) < len(board[0]) else len(board[0])
    row_size = len(board)
    col_size = len(board[0])

    for l in range(max_len, 1, -1):
        for r in range(row_size-l+1):
            for c in range(col_size-l+1):
                if isrectangle(board, r,c,l):
                    return l*l
    return 1
