def find_pos(n, value, costs, check):
    go_info = []
    for cost in costs:
        if cost[0] == n and check[cost[1]] == 0:
            go_info.append([cost[2],cost[1]])
        elif cost[1] == n and check[cost[0]] == 0:
            go_info.append([cost[2],cost[0]])
    if len(go_info) == 0 :
        return value

    go_info.sort()
    check[go_info[0][1]] = 1
    return find_pos(go_info[0][1], value+go_info[0][0], costs, check)
    
def solution(n, costs):
    result = (n-1)*n/2
    for i in range(n):
        check = [0 for _ in range(n)]
        check[i] = 1 
        answer = find_pos(i, 0, costs, check)   
        if 0 not in check:
            result = min(answer, result)
        check[i] = 0
    return result 
