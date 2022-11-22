#https://firsteast.tistory.com/103
from collections import defaultdict
from itertools import combinations
def solution(info, query):
    answer = []
    
    infos = defaultdict(list)
    for i in info:
        conditions = i.split()[:-1]
        score = int(i.split()[-1])
        for r in range(5):
            combis = list(combinations(range(4), r))
            for c in combis:
                test_cases = conditions[:]
                for v in c:
                    test_cases[v] = '-'
                infos['_'.join(test_cases)].append(score)
    for item in infos:
        infos[item].sort()
    for q in query:
        q = q.replace('and', '').split()
        conditions = '_'.join(q[:-1])
        score= int(q[-1])
        
        if conditions in list(infos):
            data = infos[conditions]
            if len(data)> 0:
                start, end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start+end) // 2] >=score:
                        end = (start+end)//2
                    else:
                        start = (start+end)//2+1
                answer.append(len(data)-start)
        else:
            answer.append(0)
    return answer
