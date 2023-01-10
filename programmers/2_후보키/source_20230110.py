from itertools import combinations
def solution(relation):
    answer = []
    row = len(relation)
    col = len(relation[0])

    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
    
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        if len(set(tmp)) != row: continue
        for x in answer:
            if set(x).issubset(set(i)):
                put = False
                break
        else:
            answer.append(i)                

    return len(answer)
