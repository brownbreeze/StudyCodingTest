def find_rst(l,w,y,x,val, maps,visited):
    visited.append([y, x])
    dr = [[-1,0,0,1],[0,-1,1,0]] #x,y
    for i in range(4):
        if y+dr[0][i] < 0 or y+dr[0][i] >= l : continue
        if x+dr[1][i] < 0 or x+dr[1][i] >= w : continue
        new_y = y+dr[0][i]
        new_x = x+dr[1][i]
        if maps[new_y][new_x] == 'X' : continue
        if (new_y,new_x) in visited : continue
        val += find_rst(l,w,new_y, new_x, int(maps[new_y][new_x]), maps,visited)
    print(val)
    return val 

def solution(maps):
    answer = []
    length = len(maps)
    width = len(maps[0])
    
    for y in range(length):
        for x in range(width):
            if maps[y][x] == 'X':continue
            print(int(maps[y][x]))
            visited =[(y,x)]
            
            answer.append(find_rst(length,width,y,x,int(maps[y][x]), maps,visited))
            
    if len(answer) == 0 :
        answer.append(-1)
    answer.sort()
    return answer
