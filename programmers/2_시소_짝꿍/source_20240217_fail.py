from itertools import combinations
def solution(weights):
    answer = 0
    li = combinations(weights, 2)
    datas = {}
    positions = [(1,1),(2, 3), (2, 4), (3, 4), (4, 3), (4, 2), (3, 2)]
    
    for a,b in li:
        flag = 0
        if a*1000+b in datas :
            answer += datas[a*1000+b]
            continue 
        if b*1000+a in datas :
            answer += datas[b*1000+a]
            continue 
        if a == b:
            answer +=1
            datas[a*1000+b] = 1
            continue
        for i,j in positions:
            if a*i == b*j:
                answer +=1
                flag = 1
                break
        datas[a*1000+b] = flag

    return answer
