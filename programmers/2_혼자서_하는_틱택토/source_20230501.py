def check(check_list, ch):
    cnt = 0
    for li in check_list:
        if li.count(ch) == 3:
            cnt +=1
    return cnt
    
def solution(board):
    answer = -1
    # check zero or start
    o_cnt = 0
    x_cnt = 0
    for row in board:
        o_cnt += row.count('O')
        x_cnt += row.count('X')
    if o_cnt+x_cnt == 0 : # first
        return 1
    elif o_cnt+x_cnt == 1:
        if o_cnt == 1: 
            return 1
        else:
            return 0
    elif o_cnt<x_cnt or o_cnt-1>x_cnt:
        return 0
    else :
        # check 대각선
        check_list = [row for row in board]
        for i in range(3):
            check_list.append([board[0][i],board[1][i], board[2][i]])
        check_list.append([board[0][0],board[1][1], board[2][2]])
        check_list.append([board[0][2],board[1][1], board[2][0]])
        # print(check_list)
        o_win_cnt = check(check_list, 'O')
        x_win_cnt = check(check_list, 'X')
        if o_win_cnt >= 1:
            if x_win_cnt == 0 and o_cnt == x_cnt+1:
                return 1
            else:
                return 0
        elif x_win_cnt >= 1:
            if o_win_cnt == 0 and o_cnt == x_cnt:
                return 1
            else:
                return 0
    return 1
