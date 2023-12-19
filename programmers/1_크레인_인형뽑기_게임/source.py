def solution(board, moves):
    answer = 0
    basket = []
    
    row_len = len(board)
    col_len = len(board[0])
    stacks = [[] for _ in range(row_len)]
    
    for r in range(row_len-1, -1, -1):
        for c in range(col_len):
            if board[r][c]!=0:
                stacks[c].append(board[r][c])
    for move in moves:
        m = move-1
        if len(stacks[m]) != 0:
            b = stacks[m].pop()
            if len(basket) != 0 and basket[-1] == b:
                basket.pop()
                answer +=2
            else:
                basket.append(b)
    # print(stacks)            
    return answer
