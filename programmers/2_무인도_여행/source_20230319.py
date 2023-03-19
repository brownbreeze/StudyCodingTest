dr = [[-1,0,0,1],[0,-1,1,0]] #x,y

def solution(maps):
    answer = []
    length = len(maps)
    width = len(maps[0])
    visited = [[0 for _ in range(width)] for _ in range(length)]
    for y in range(length):
        for x in range(width):
            if maps[y][x] == 'X' or visited[y][x] == 1:continue
            que = [(y,x)]
            temp_rst = 0 
            while True:
                if len(que) == 0 : break
                go_y, go_x = que.pop()
                if visited[go_y][go_x] == 1 : continue
                visited[go_y][go_x] = 1
                temp_rst += int(maps[go_y][go_x])
                for i in range(4):
                    n_y = go_y + dr[0][i]
                    n_x = go_x + dr[1][i]
                    if n_y >=0 and n_y < length and n_x >=0 and n_x <width and visited[n_y][n_x] == 0 and maps[n_y][n_x] != 'X':
                        que.append((n_y,n_x))
                
            answer.append(temp_rst)
            
    if len(answer) == 0 :
        answer.append(-1)
    answer.sort()
    return answer
