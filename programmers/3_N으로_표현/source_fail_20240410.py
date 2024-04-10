from itertools import combinations_with_replacement
def solution(N, number):
    answer = 0
    d = dict()
    arr = list()
    d[N] = 1
    arr.append(N)
    
    t = N
    for i in range(1,9):
        d[t*10 + N] = i+1
        t = t*10 + N
        arr.append(t)
        
    def get_values(b):
        ar = list()
        # print(len(b))
        for a1, a2 in b:
            c = d[a1] + d[a2]
            if c > 8: 
                print(a1, a2, d[a1], d[a2])
                break
            
            t = a1*a2
            ar.append(t)
            if t not in d:
                d[t] = c
            else:
                d[t] = min(d[t], c)
            t = a1+a2
            ar.append(t)
            if t not in d:
                d[t] = c
            else:
                d[t] = min(d[t], c)
            t = a1-a2
            ar.append(t)
            if t not in d:
                d[t] = c
            else:
                d[t] = min(d[t], c)
            t = a2-a1
            ar.append(t)
            if t not in d:
                d[t] = c
            else:
                d[t] = min(d[t], c)
                
            if a2!=0:
                t = a1//a2
                ar.append(t)
                if t not in d:
                    d[t] = c
                else:
                    d[t] = min(d[t], c)
                    
            if a1!=0: 
                t = a2//a1
                ar.append(t)
                if t not in d:
                    d[t] = c
                else:
                    d[t] = min(d[t], c)
        return ar
    
    
    for i in range(8):
        
        b = list(combinations_with_replacement(arr, 2))
        t = get_values(b)
        arr.extend(t)
        arr = list(set(arr))
        
    if number in d:
        return d[number]
    return -1
# 왜 안될까?? 8을 넘겨야하는 경우가 매우 많아야하는데 해결이 되지 않음 

