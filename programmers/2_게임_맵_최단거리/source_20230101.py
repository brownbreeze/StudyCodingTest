from collections import deque
def solution(maps):
    answer = 0
    arr = deque()
    arr.append([0,0,0])
    maps[0][0] = -1
    answer = bfs(maps, arr, [len(maps), len(maps[0])])
    return answer

def bfs(maps, arr, correct):
    go_pos = [[-1,0,0,1],[0,-1,1,0]]
    while True:
        if len(arr) == 0 : break
        data = arr.popleft()
        for i in range(4):
            new_y = data[0] + go_pos[0][i]
            new_x = data[1] + go_pos[1][i]
            if new_y == correct[0]-1 and new_x == correct[1]-1:
                return data[2]+2
            if new_y not in range(correct[0]) or new_x not in range(correct[1]):
                continue
            if maps[new_y][new_x] == 1:
                maps[new_y][new_x] = -1
                arr.append([new_y, new_x, data[2]+1])       
    return -1
