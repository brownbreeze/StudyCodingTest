def solution(park, routes):
    answer = []
    park_map = [[0 for _ in range(50)] for _ in range(50)]
    pos_val = {'N':0, 'S':2, 'W':3,'E':1}
    mov_map = [[-1,0,1,0],[0,1,0,-1]]
    
    s_r, s_c = 0,0
    row_len = len(park)
    col_len = len(park[0])
    for r in range(row_len):
        for c in range(col_len):
            if park[r][c] == "S":
                s_r = r
                s_c = c
    
    for route in routes:
        val = route.split(" ")
        t_r = s_r
        t_c = s_c
        val[1] = int(val[1])
        for m in range(val[1]):
            t_r += mov_map[0][pos_val[val[0]]]
            t_c += mov_map[1][pos_val[val[0]]]
            if t_r in range(0,row_len) and t_c in range(0, col_len):
                if park[t_r][t_c] !="X":
                    continue
                else:
                    break
            else:
                break
        else: # okay
            s_r = t_r
            s_c = t_c
            continue        
    return [s_r, s_c]

