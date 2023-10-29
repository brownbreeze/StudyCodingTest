from collections import deque

def rotate(map):
    y_pos = -1
    x_pos = -1
    result = []
    
    table = [[0 for _ in range(6)] for _ in range(6)]
    result = [[0 for _ in range(6)] for _ in range(6)]
    for i in range(6):
        for j in range(6):
            table[j][5-i] = map[i][j]
    
    for i in range(6):
        for n in table[i]:
            if n == 1:
                y_pos = i
                break
        if y_pos != -1: 
            break
    
    for i in range(6):
        for j in range(6):
            if table[j][i] == 1:
                x_pos = i
                break
        if x_pos != -1:
            break
            
    for i in range(y_pos, 6):
        for j in range(x_pos, 6):
            result[i-y_pos][j-x_pos] = table[i][j]
    # print("rotate") 
    # for i in result:
    #     print(i)
    # print()
    return result 

def get_size(table):
    cnt = 0
    for i in range(6):
        for j in range(6):
            if table[i][j]:
                cnt = cnt +1
    return cnt

def is_match(map1, map2):
    result = 0
    fail_flag = 0
    # print('is_match')
    # print('map1')
    # for i in map1:
    #     print(i)
    # print('map2')
    # for i in map2:
    #     print(i)
    # print()
    
    temp = map2
    for i in range(4):
        result = 0
        fail_flag = 0
        temp = rotate(temp)
        # temp = map2
        for r in range(6):
            for c in range(6):
                if map1[r][c] != temp[r][c]: 
                    fail_flag = 1
                    break
            if fail_flag == 1:
                break
        if fail_flag == 0:
            # print('success' , get_size(temp))
            return get_size(temp)
    return -1
    
def regul(maps):# 50*50 -> 6*6
    y_pos = -1
    x_pos = -1
    
    result = [[0 for _ in range(6)] for _ in range(6)]
    
    for i in range(50):
        for n in maps[i]:
            if n == 1:
                y_pos = i
                break
        if y_pos != -1: 
            break
    
    for i in range(50):
        for j in range(50):
            if maps[j][i] == 1:
                x_pos = i
                break
        if x_pos != -1:
            break
    
    max_y = y_pos + 6 if y_pos+6 <=50 else 50
    max_x = x_pos + 6 if x_pos+6 <=50 else 50
    for i in range(y_pos, max_y):
        for j in range(x_pos, max_x):
            result[i-y_pos][j-x_pos] = maps[i][j]
    # for i in range(y_pos, y_pos+6):
    #     result.append(maps[i][x_pos:x_pos+6])
    
    # for i in result:
    #     print(i)
    # print()
    return result
        
    
def get_zogak(n, y,x,r_s, c_s,table):
    # print(y,x)
    val = [[0 for _ in range(51)] for _ in range(51)]
    go_pos = [[-1,0,1,0], [0,-1,0,1]]
    arr =  deque()
    val[y][x] = 1
    arr.append([y,x])
    while True:
        if len(arr)==0:break
        data = arr.popleft()
        for i in range(4):
            ny = data[0] + go_pos[0][i]
            nx = data[1] + go_pos[1][i]
            if ny not in range(0,r_s) or nx not in range(0,c_s): continue
            if table[ny][nx] == n and val[ny][nx] == 0:
                arr.append([ny, nx])
                # print('+',ny,nx)
                val[ny][nx] = 1
                table[ny][nx] = 0 if n == 1 else 1 
    return regul(val)
    
def get_items(n, table):
    arr = []
    r_s = len(table)
    c_s = len(table[0])
    for y in range(r_s):
        for x in range(c_s):
            if table[y][x] == n:
                arr.append(get_zogak(n,y,x,r_s, c_s,table))
    return arr
    
def solution(game_board, table):
    answer = 0
    
    board_zeros = get_items(0, game_board) # 0인 아이템들 가져오기 
    table_ones = get_items(1, table) # 1인 아이템들 가져오기
    
    board_zogak_size = len(board_zeros)    
    table_zogak_size = len(table_ones)    
    arr = [0 for _ in range(table_zogak_size)]
    
    for b in range(board_zogak_size):
        for i in range(table_zogak_size):
            if arr[i] == 1: continue  # already used
            check = is_match(board_zeros[b], table_ones[i])
            if check != -1:
                arr[i] = 1
                answer = answer + check 
                break
                
    return answer
