#DFS
# DFS
def isInRange(r, c, row_len, col_len):
    return (r >= 0 and r < row_len) and (c >= 0 and c < col_len)

def numIslands(grid):
    number_of_islands = 0
    row_len = len(grid)
    col_len = len(grid[0])
    visited = [[False] * col_len for _ in range(row_len)]

    def dfs(r, c):
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        visited[r][c] = True
        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]
						if isInRange(next_r, next_c, row_len, col_len):
            # if next_r >= 0 and next_r < row_len and next_c >= 0 and next_c < col_len:
                if grid[next_r][next_c] == "1" and not visited[next_r][next_c]:
                    dfs(next_r, next_c)

    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == "1" and not visited[i][j]:
                dfs(i, j)
                number_of_islands += 1

    return number_of_islands
