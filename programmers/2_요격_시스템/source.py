from itertools import combinations
def solution(targets):
    answer = 0
    d = {}
    i = 0
    tl = len(targets)
    values = [i for i in range(1,tl+1)]
    for a,b in targets:
        for x in range(a,b+1):
            if x in d:
                d[x].append(i)
            else:
                d[x] = [i]
        i+=1
    keys = sorted(list(d.keys()))
    max_key = keys[-1]
    for i in range(1,max_key+1):
        checks = list(combinations(keys, i))
        for check in checks:
            temp = set()
            for j in list(check):
                temp = temp | set(d[j])
            if len(temp) == tl:
                return i
    return answer
