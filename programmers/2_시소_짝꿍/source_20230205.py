import itertools 

def solution(weights):
    answer = 0
    weights.sort()
    c = list(itertools.combinations(weights, 2))
    for value in c:
        i, j = value
        if i == j : 
            answer +=1
            continue
        set_i = {i*m for m in [3,4]}
        set_j = {j*m for m in [2,3]}
        if set_i.intersection(set_j):
            answer +=1
    return answer
