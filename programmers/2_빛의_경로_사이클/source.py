def get_f(st_y,st_x,st_d,d):
    return f"{st_y},{st_x},{st_d},{d}" 
    
def solution(grid):
    answer = []
    d_pos = [[0,-1,0,1],[1,0,-1,0]]

    rl = len(grid)
    cl = len(grid[0])
    maps = [[[[0,0] for _ in range(4)] for _ in range(cl)] for _ in range(rl)]
    
    sc_d = {}
    def get_next(y,x,d,subd):
        if grid[y][x] == 'R':
            d += 1
        elif grid[y][x] == 'L':
            d -= 1
        d = (d+4)%4
        y += d_pos[0][d]
        x += d_pos[1][d]
        y = (y+rl)%rl
        x = (x+cl)%cl
        return y,x,d
        
    go_list = []
    for y in range(rl):
        for x in range(cl):
            for i in range(4):
                # 모든 경우의 수 ..ㅋㅋ 
                go_list.append([y,x,i])
                # sc_d 에다가 적립해서 방문 경험이 있으면 시도 안할 예정! 
    
    while go_list:
        g = go_list.pop()
        sy = g[0]
        sx = g[1]
        sd = g[2]
        f = get_f(sy,sx,sd,1)
        if f in sc_d:
            continue
        sc_d[f] = 1
        y, x, d = sy, sx, sd
        cnt = 0
        while True:
            cnt += 1
            # print(y,x,d)
            y,x,d = get_next(y,x,d,1)
            # print(y,x,d)
            # print()
            # break
            if sy==y and sx == x and sd == d:
                answer.append(cnt)
                break
            f = get_f(y,x,d,1) 
            if f in sc_d:
                break
            sc_d[f] = 1
        # break
    # print(sc_d)
    answer.sort()       
    return answer
