from collections import deque
class Pos:
    def __init__(self, a,b):
        self.x = a
        self.y = b
    def __repr__(self):
        return f'{self.y}, {self.x}'
    
dir_pos = [[-1,0,1,0], [0,-1,0,1]]
visited = list()

def get_path(maps, rc, cc, pos_f, pos_t):    
    have_to = deque()
    have_to.append([pos_f, 0])   
    # global visited
    
    while have_to:
        p, c = have_to.popleft()
        print(c,'----', p, '---',len(have_to))
        if visited[p.y*cc+p.x] == 1:
            continue 
        visited[p.y*cc +p.x] = 1
        
        if p.y == pos_t.y and p.x == pos_t.x:
            return c
        for i in range(4):
            new_y = p.y+dir_pos[0][i]
            new_x = p.x+dir_pos[1][i]
            print('> ', new_y,new_x)
            if new_y >= 0 and new_y < rc and new_x >= 0 and new_x < cc:
                if maps[new_y*cc+new_x] ==19 :
                    continue
                elif visited[new_y*cc+new_x]==1:
                    continue
            else:
                continue
            have_to.append([Pos(new_y, new_x), c+1])

            
    # print('fail')
    return -1        
    
    
def solution(maps):
    val = dict()
    global visited
    rowcnt = len(maps)
    colcnt = len(maps[0])
    
    num_map = [0 for _ in range(rowcnt*colcnt)]
    visited = [0 for _ in range(rowcnt*colcnt)]
    
    for y in range(rowcnt):
        for x in range(colcnt):
            if maps[y][x] in ['S', 'L', 'E']: 
                val[maps[y][x]] = Pos(x,y)
            num_map[y*colcnt+x] = ord(maps[y][x])-69 # 14-> S, 10->O, 7->L, 19 ->X, 0-> E

    answer = get_path(num_map, rowcnt,colcnt,val['S'], val['L'])
    if answer == -1:
        return answer
    # visited = [0 for _ in range(rowcnt*colcnt+1)]
    # answer2 = get_path(num_map, rowcnt, colcnt, val['L'], val['E'])
    # if answer2 == -1:
    return -1
    # return answer+answer2+1
