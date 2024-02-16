from itertools import combinations
def solution(weights):
    answer = 0
    li = combinations(weights, 2)

    for a,b in li:
        flag = 0
        # print(a,b)
        for i in range(2,5):
            if flag: 
                break
            for j in range(2,5):
                if a*i == b*j:
                    answer +=1
                    flag = 1

    return answer
