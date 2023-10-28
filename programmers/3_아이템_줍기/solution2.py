from collections import deque

def check_can_go(maps, y, x, d):
    go_pos = [[-1,0,1,0], [0,-1,0,1]]
    ny = y + go_pos[0][d]
    nx = x + go_pos[1][d]
    if ny not in range(0,102) or nx not in range(0,102) : return False
    if maps[ny][nx] == 9: 
        return True
    return False

def bfs(maps, arr, toy, tox):
    go_pos = [[-1,0,1,0],[0,-1,0,1]]
    while True:
        if len(arr) == 0 : break
        data = arr.popleft() # cnt, y, x, dir      
        if data[1] == toy and data[2] == tox: return data[0]
        for i in range(4):
            if (i+2)%4 == data[3] : continue
            if check_can_go(maps, data[1], data[2], i):
                arr.append([data[0]+1, data[1]+go_pos[0][i], data[2]+go_pos[1][i], i])
    
    return -1

def solution(rectangle, characterX, characterY, itemX, itemY):
    maps =[[0 for _ in range(51*2)] for _ in range(51*2)]
    go_pos = [[-1,0,1,0],[0,-1,0,1]]
    for rec in rectangle:
        lx, ly, rx, ry = rec
        for y in range(ly*2, (ry+1)*2-1):
            for x in range(lx*2, (rx+1)*2-1):
                if maps[y][x] == 0 or  maps[y][x] == 9 :
                    if lx*2 == x or ly*2 == y or ry*2 == y or rx*2 == x:
                        maps[y][x] = 9
                    else:
                        maps[y][x] = 2
    total_len = 0
    for y in range(0, 102):
        for x in range(0, 102):
            total_len = total_len+1 if maps[y][x]==9 else total_len

    arr = deque()      
    for i in range(4):
        arr.append([0, characterY*2, characterX*2, i]) 
    result = bfs(maps, arr, itemY*2, itemX*2)
    return result//2
