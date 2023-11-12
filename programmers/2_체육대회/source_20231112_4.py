answer = 0
def dfs(gpos, points, s_len, g_len, ability, check):
    global answer 
    if gpos >= g_len :
        answer = max(points, answer)
        return 
    for i in range(s_len):
        if check[i] == 0 :
            check[i] = 1 
            dfs(gpos+1, points+ability[i][gpos], s_len, g_len, ability, check)
            check[i] = 0
            
def solution(ability):
    global answer    
    s_len = len(ability)
    g_len = len(ability[0])
    check = [0 for _ in range(s_len)]
    dfs(0, 0, s_len, g_len, ability, check)
    return answer
