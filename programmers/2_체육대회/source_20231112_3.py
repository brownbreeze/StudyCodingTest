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
