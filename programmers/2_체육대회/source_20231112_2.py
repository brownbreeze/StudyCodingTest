def solution(ability):
    answer = 0
    s_len = len(ability)
    g_len = len(ability[0])
    
    check_list = []
    pos = 0 
    for i in range(s_len):
        check_list.append([[i],1, ability[i][0]])
    
    while True:
        if len(check_list) == 0 : break 
        history, pos, points = check_list.pop()
        if pos >= g_len : 
            answer = points if points > answer else answer
            continue
        for i in range(s_len):
            if i in history : continue
            temp = history.copy()
            temp.append(i)
            check_list.append([temp, pos+1, points+ability[i][pos]])
        
    return answer
