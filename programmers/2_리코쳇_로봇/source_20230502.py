from collections import deque

def go_to(board, cur_x, cur_y, d,  width, height):
    dirs = [[-1,0,1,0],[0,-1,0,1]]
    cnt = 0
    go_x = cur_x
    go_y = cur_y

    while True:
        if go_x + dirs[1][d] < 0 or go_x + dirs[1][d] >= width or \
            go_y + dirs[0][d] < 0 or go_y + dirs[0][d] >= height:
            if cnt == 0: 
                return -1,-1
            return go_x, go_y
        if board[go_y+dirs[0][d]][go_x+dirs[1][d]] == 'D':
            return go_x, go_y
        go_x += dirs[1][d]
        go_y += dirs[0][d]
        cnt += 1
        
    return -1,-1
    
def solution(board):
    answer = 0
    
    # dirs = [[-1,0,1,0],[0,-1,0,1]]
    que = deque([])
    
    # find R 
    width = len(board[0])
    height = len(board)
    r_x = 0
    r_y = 0
    find_flag = False
    for x in range(width):
        for y in range(height):
            if board[y][x] == 'R':
                r_x = x
                r_y = y
                find_flag = True
                break
        if find_flag : 
            break
    
    # input start point 
    for dir in range(4):
        que.append((r_x, r_y, 0, dir))
    
    # copy visited
    visited = [[[0,0,0,0] for _ in range(width)] for _ in range(height)]
    
    # go que 
    while True:
        print()
        if len(que) <= 0 :
            break
        cur_x, cur_y, cnt, d = que.popleft()
        # print('pop left', cur_y, cur_x, cnt, d)
        go_x, go_y = go_to(board, cur_x, cur_y, d, width, height)
        # print('go : ', go_y, go_x)
        if go_x == -1:
            # print('cant go')
            continue
        if visited[go_y][go_x][d] == 1:
            # print('already visited')
            continue
        visited[go_y][go_x][d] = 1
        # print('current', board[go_y][go_x])
        if board[go_y][go_x] == 'G':
            return cnt+1
        
        for dir in range(4):
            que.append((go_x, go_y, cnt+1, dir))
    return -1
