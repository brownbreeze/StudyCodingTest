from itertools import combinations
def solution(targets):
    values = {}
    i = 0
    for s,e in targets:
        for x in range(s,e):
            if x in values:
                values[x].append(i)
            else:
                values[x] = [i]
        i += 1
    tl = len(targets)
    keys = values.keys()
    kl = len(keys)
    for i in range(1, kl+1):
        c = combinations(keys, i)
        for l in c:
            val = set()
            for x in l:
                val = val | set(values[x])
            if len(val) == tl:
                return i
    return -1
