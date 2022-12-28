v_dir=[[0,1],[1,0],[0,-1],[-1,0]]
max_y = 0
max_x = 0
real_maps = [[]]
def go_find(me, final, dont_go, cnt):
    global v_dir
    global max_y
    global max_x
    global real_maps
    if me == final:
        return cnt
    for i in range(4):
        if dont_go == i: continue
        new_y = v_dir[i][0] + me[0]
        new_x = v_dir[i][1] + me[1]
        
        if new_y in range(0,max_y) and new_x in range(0,max_x) and real_maps[new_y][new_x] == 1:
            real_maps[new_y][new_x] = -1
            val = go_find([new_y,new_x], final, (i+2)%4, cnt+1)
            if val == -1:
                continue
            return val
    return -1
        
def solution(maps):
    answer = 0 
    me = [0,0] # y,x
    final = [len(maps)-1, len(maps[0])-1]
    global max_y
    global max_x
    global real_maps
    real_maps = maps
    max_y = len(maps)
    max_x = len(maps[0])
    answer = go_find(me, final, dont_go=-1, cnt = 1)
    return answer
