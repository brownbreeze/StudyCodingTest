def solution(dirs):
    answer = 0
    arr = [[[0,0,0,0] for _ in range(11)] for _ in range(11)]
    d_pos = {'U':0, 'R':1, 'D':2, 'L':3}
    valmove = [[-1,0,1,0],[0,1,0,-1]] # y, x
    
    x = 5
    y = 5
    for d in dirs:
        ny = valmove[1][d_pos[d]]
        nx = valmove[0][d_pos[d]]    
        if x+nx not in range(0,11) or y+ny not in range(0,11):
            continue
        if arr[y][x][d_pos[d]] == 0 : 
            arr[y][x][d_pos[d]] = 1
            answer +=1
        x += nx
        y += ny
        arr[y][x][(d_pos[d]+2)%4] = 1
    return answer
