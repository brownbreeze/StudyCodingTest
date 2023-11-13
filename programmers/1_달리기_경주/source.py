def solution(players, callings):
    answer = []
    l_p = len(players)
    per_dict = dict()
    num_dict = dict()
    for i in range(l_p):
        num_dict[i] = players[i]
        per_dict[players[i]] = i
    for name in callings:
        pos = per_dict[name]
        conv_pos = pos - 1
        conv_name = num_dict[pos-1]
        per_dict[name] = pos -1 
        per_dict[conv_name] = pos
        num_dict[pos] = conv_name
        num_dict[pos-1] = name
    for k in num_dict:
        answer.append(num_dict[k])
    return answer
