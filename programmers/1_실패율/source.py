from collections import Counter
def solution(N, stages):
    answer = []
    c = Counter(stages)
    # print(c)
    cnt = len(stages)
    for i in range(1, N+1):
        if cnt == 0 :
            answer.append([0, i])
        else:
            answer.append([-c[i]/cnt,i])
        cnt -= c[i]
    answer.sort()
    return [b for a,b in answer]
