def check(i , j):
    if i == j : return 1
    set_i = {i*m for m in [2,3,4]}
    set_j = {j*m for m in [2,3,4]}
    if set_i.intersection(set_j):
        return 1
    return 0
    
def solution(weights):
    answer = 0
    len_weig = len(weights)
    for i in range(len_weig):
        for j in range(i+1, len_weig):
            answer+=check(weights[i],weights[j])
    return answer
