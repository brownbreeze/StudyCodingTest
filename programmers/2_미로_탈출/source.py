from collections import deque
class Pos:
    def __init__(self, a,b):
        self.x = a
        self.y = b
    def __repr__(self):
        return f'{self.y}, {self.x}'

def get_path(maps, rc, cc, pos_f, pos_t):
    dir_pos = [[-1,0,1,0], [0,-1,0,1]]
    have_to = deque()
    maps[pos_f.y][pos_f.x] = 19
    have_to.append([pos_f,maps.copy(), 0])    
    
    while have_to:
        p, m, c = have_to.popleft()
        # print(p,'->',c, len(have_to), m)
        if p.y == pos_t.y and p.x == pos_t.x:
            return c
        for i in range(4):
            new_y = p.y+dir_pos[0][i]
            new_x = p.x+dir_pos[1][i]
            if new_y in range(rc) and new_x in range(cc):
                if m[new_y][new_x] ==19 :
                    continue
            else:
                continue
            m[new_y][new_x] = 19
            have_to.append([Pos(new_y, new_x), m.copy(), c+1])
            m[new_y][new_x] = 10
            
    # print('fail')
    return -1        
    
    
def solution(maps):
    rowcnt = len(maps)
    colcnt = len(maps[0])
    
    val = dict()
    num_map = []

    for y in range(rowcnt):
        temp = []
        for x in range(colcnt):
            if maps[y][x] in ['S', 'L', 'E']: 
                val[maps[y][x]] = Pos(x,y)
            temp.append(ord(maps[y][x])-69) # 14-> S, 10->O, 7->L, 19 ->X, 0-> E
        num_map.append(temp)
    # print(val)
    # print(num_map)
    # return -1
    answer = get_path(num_map, rowcnt,colcnt,val['S'], val['L'])
    print(answer)
    if answer == -1:
        return answer
    answer2 = get_path(num_map, rowcnt, colcnt, val['L'], val['E'])
    print(answer2)
    if answer2 == -1:
        return -1
    return answer+answer2+1
