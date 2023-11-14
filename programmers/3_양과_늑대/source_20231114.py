def solution(info, edges):
    visited = [0 for _ in range(len(info))]
    answer = []
    
    def DFS(y, n):
        if y > n:
            answer.append(y)
        else:
            return
        
        for s,e in edges:
            if visited[s] and not visited[e]:
                visited[e] = 1
                if info[e]:
                    DFS(y, n+1)
                else:
                    DFS(y+1, n)
                visited[e] = 0
    visited[0] = 1
    DFS(1,0)
    
    return max(answer)
