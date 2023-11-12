# timeover
>  왜 ... 아래 두 소스가 속도가 다를까? 1번 소스는 심지어 상위 3개 커트로 한번 더 걸러준 소스인데,, 
1. 1번 소스
```
def solution(ability):
    answer = 0
    s_len = len(ability)
    g_len = len(ability[0])
    
    check_list = []
    pos = 0 
    
    g_max_list = []
    for i in range(g_len):
        temp = []
        for j in range(s_len):
            temp.append(ability[j][i])
        temp.sort()
        g_max_list.append(temp)
        
        
    for i in range(s_len):
        if ability[i][0] < g_max_list[0][-g_len]: continue
        check_list.append([[i],1, ability[i][0]])
    # print(check_list)
    
    while True:
        if len(check_list) == 0 : break 
        history, pos, points = check_list.pop()
        if pos >= g_len : 
            answer = points if points > answer else answer
            continue
        for i in range(s_len):
            if i in history : continue
            if ability[i][pos] < g_max_list[pos][-g_len]: continue
            temp = history.copy()
            temp.append(i)
            check_list.append([temp, pos+1, points+ability[i][pos]])
        
    return answer
```

2. 2번 소스 
```
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
```

