def solution(board, h, w):
    answer = 0
    d = [[0, 1, -1, 0], [1, 0, 0, -1]]
    
    hl = len(board)
    wl = len(board[0])
    
    h = int(h)
    w = int(w)
    c = board[h][w]
    for i in range(4):
        dw = d[0][i]
        dh = d[1][i]
        h_check = h+dh
        w_check = w+dw
        if h_check in range(0, hl) and w_check in range(0, wl):
            if board[h_check][w_check] == c:
                answer +=1     
    
    return answer
