def all_visited(data):
    for key in data.keys():
        for da in data[key]:
            if da[1] == 0 : return False
    return True

def go_find(data,  answer, pos_str):
    if all_visited(data) : 
        return 1
    if pos_str in data:
        for set_data in data[pos_str]:
            if set_data[1] == 1: continue
            answer.append(set_data[0])
            set_data[1] = 1
            d = go_find(data, answer, set_data[0])
            if d == 1: return 1
            set_data[1] = 0
            answer.pop()
    else:
        return -1
    
def solution(tickets):
    answer = []
    data = dict()
    tickets.sort()
    for ticket in tickets : 
        if ticket[0] in data:
            data[ticket[0]].append([ticket[1],0])
        else:
            data[ticket[0]] = [[ticket[1],0]]
    answer.append('ICN')
    go_find(data, answer,'ICN')
    return answer
