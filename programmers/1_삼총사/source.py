from itertools import combinations, permutations

def solution(number):
    answer = 0
    combi = list(combinations(number, 3))
    # print(combi)
    for cob in combi:
        if sum(list(cob)) == 0:
            answer +=1
    return answer
