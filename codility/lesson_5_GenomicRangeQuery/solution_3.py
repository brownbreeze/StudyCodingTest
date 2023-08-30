def solution(S, P, Q):
    dic = {'A':1, 'C':2, 'G':3, 'T':4}
    arr = [dic[s] for s in S]

    mp = list()    
    base = [ 0 for _ in range(4)]
    for s in arr:
        base[s-1] +=1
        mp.append(base.copy())
    
    lenP = len(P)
    result = list()
    for i in range(lenP):
        for j in range(4):
            if mp[Q[i]][j] - mp[P[i]][j] > 0 :
                result.append(j+1)
                break
        else : 
            result.append(4)
    return result
