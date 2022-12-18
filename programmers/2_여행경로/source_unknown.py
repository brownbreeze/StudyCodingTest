def go_travel(tks, vis, cur, cnt):
    if 0 not in vis:
        #print("yes~")
        return 1
    for i in range(len(tks)):
        a,b = tks[i]
        if a != cur or vis[i] != 0 : continue
        vis[i] = cnt+1
        num = go_travel(tks, vis, b, cnt+1)
        if num == 1 : return 1
        vis[i] = 0
    return -1
    
def solution(tickets):
    answer = []
    visited = [0 for _ in tickets]
    tickets.sort()
    print(tickets)
    for i in range(len(tickets)):
        a,b = tickets[i]
        if a != "ICN": continue
        visited[i] = 1
        num = go_travel(tickets, visited, b, 1)
        if num == 1 : break
        visited[i] = 0
    for i in range(1,len(visited)+1):
        idx = visited.index(i)
        answer.append(tickets[idx][0])
        if i == len(visited):
            answer.append(tickets[idx][1])
    return answer
