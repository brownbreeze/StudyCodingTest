from collections import deque

def get_dir(y, x, d, left_zero, maps):
    go_pos = [[-1,0,1,0],[0,-1,0,1]]
    i = d
    fy = y + go_pos[0][i]
    fx = x + go_pos[1][i]
    ry = y + go_pos[0][(i+1)%4]
    rx = x + go_pos[1][(i+1)%4]
    ly = y + go_pos[0][(i+3)%4]
    lx = x + go_pos[1][(i+3)%4]

    if maps[ry][rx] + maps[ly][lx] + maps[fy][fx] == 3:
        if left_zero :
            return (i+3)%4
        else :
            return (i+1)%4
    elif maps[ry][rx] == 1 and maps[ly][lx]==0 and maps[ry][rx] == 0 :
        return i
    elif maps[ry][rx] == 0:
        if maps[ry][rx] == 1:
            return (i+1)%4
        elif maps[ly][lx] == 1:
            return (i+3)%4            
    return -1
            
def bfs(maps, arr, toy, tox):
    go_pos = [[-1,0,1,0],[0,-1,0,1]]
    while True:
        if len(arr) == 0 : break
        data = arr.pop()
        d = get_dir(data[0], data[1], data[2], data[3], maps)
        print(data,'d', d)
        if d == -1 : 
            print(data[2])
            continue 
        ny = data[0] + go_pos[0][d]
        nx = data[1] + go_pos[1][d]
        if ny == toy and nx == tox : 
            return data[3]+1
        arr.append([ny, nx, d, data[3], data[4]+1])
    return -1

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    maps =[[0 for _ in range(50)] for _ in range(50)]
    go_pos = [[-1,0,1,0],[0,-1,0,1]]
    for rec in rectangle:
        lx, ly, rx, ry = rec
        for y in range(ly, ry+1):
            for x in range(lx, rx+1):
                maps[y][x] = 1
    arr = deque()
    for i in range(4):
        
        lef_y = characterY + go_pos[0][(i+3)%4]
        lef_x = characterX + go_pos[1][(i+3)%4]
        arr.append([characterY, characterX, i, (maps[lef_y][lef_x]==0), 0])
    return bfs(maps, arr, itemY, itemX)
