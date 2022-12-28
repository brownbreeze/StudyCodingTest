v_dir=[[0,1],[1,0],[0,-1],[-1,0]]
max_y = 0
max_x = 0
def go_find(me, final, maps, dont_go, cnt):
    global v_dir
    global max_y
    global max_x
    # print(f'{cnt}, {me}, {final}, {dont_go}')
    if cnt == 10000: 
        return -1
    # print(v_dir, max_y, max_x)
    if me == final:
        # print('ye~')
        return cnt
    for i in range(4):
        if dont_go == i: continue
        new_y = v_dir[i][0] + me[0]
        new_x = v_dir[i][1] + me[1]
        # print(f'  > check {new_y},{new_x}')
        if new_y in range(0,max_y) and new_x in range(0,max_x) and maps[new_y][new_x] == 1:
            val = go_find([new_y,new_x], final, maps, (i+2)%4, cnt+1)
            if val == -1:
                maps[new_y][new_x] = -1
                continue
            return val
    
    maps[me[0]][me[0]] = -1
    return -1
        
def solution(maps):
    answer = 0 
    me = [0,0] # y,x
    final = [len(maps)-1, len(maps[0])-1]
    print(me, final)
    global max_y
    global max_x
    max_y = len(maps)
    max_x = len(maps[0])
    answer = go_find(me, final, maps, dont_go=-1, cnt = 1)
    return answer
