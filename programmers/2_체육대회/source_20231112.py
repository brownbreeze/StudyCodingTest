def solution(ability):
    answer = 0
    s_len = len(ability)
    g_len = len(ability[0])
    
    check_list = []
    for i in range(s_len):
        check_list.append([[i],1,ability[i][0]])
        
    while True:
        if len(check_list) == 0 : break
        history, gpos, value = check_list.pop()
        if gpos >= g_len:
            answer = value if answer < value else answer
            continue
        max_points = 0
        for i in range(s_len):
            if i in history: continue
            max_points = max_points if max_points > ability[i][gpos] else ability[i][gpos]
        for i in range(s_len):
            if i in history: continue
            if ability[i][gpos] == max_points:
                temp_history = history
                temp_history.append(i)
                check_list.append([temp_history, gpos+1, value+max_points])
    
    return answer
