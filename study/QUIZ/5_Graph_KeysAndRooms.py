def canVisitAllRoos(rooms):
    # visited = [] 
    visited = dict()
    
    # v에 연결된 V에 방문 할것이다
    def dfs(v):
        # visited.append(v)
        visited[v] = True
        for next_v in rooms[v]:
            if next_v not in visited:
                dfs(next_v)
            # if next_v not in visited:
            #     dfs(next_v)
    
    dfs(0)
    if len(visited) == len(rooms):
        return True 
    else:
        return False


rooms = [[1,3],[2,4],[0],[4],[],[3,4]]
print(canVisitAllRoos(rooms))