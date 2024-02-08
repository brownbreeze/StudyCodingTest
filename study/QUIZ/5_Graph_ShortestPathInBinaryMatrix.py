from collections import deque

def shortestPathBinaryMatrix(grid):
    sortest_path_len = -1
    row = len(grid)
    col = len(grid[0])

    # 방얼직 
    if grid[0][0] != 0 and grid[row-1][col-1] != 0:
        return sortest_path_len

    visited = [[False]*col for _ in range(row)]
    dr = [-1,-1,-1,0,0,1,1,1]
    dc = [-1,0,1,-1,1,-1,0,1]

    queue = deque()
    queue.append((0,0,1))
    visited[0][0] = True
    while queue:
        cur_r,cur_c, cur_l= queue.popleft()
        # 목적지 도착 확인 
        if cur_r == row-1 and cur_c == col-1:
            sortest_path_len = cur_l
            break

        for i in range(8):
            new_r = cur_r + dr[i]
            new_c = cur_c + dc[i]
            if new_r >=0 and new_r <row and new_c >= 0 and new_c < col:
                if grid[new_r][new_c] == 0 and not visited[new_r][new_c] :
                    queue.append((new_r, new_c, cur_l+1))
                    visited[new_r][new_c] = True 
     
    return sortest_path_len

grid = [
    [0,0,0],
    [1,1,0],
    [1,1,0]
]
print(shortestPathBinaryMatrix(grid))