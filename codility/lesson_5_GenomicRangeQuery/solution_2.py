def solution(S, P, Q):
    dic = {'A':1, 'C':2, 'G':3, 'T':4}
    arr = [dic[s] for s in S]
    lenP = len(P)
    lenN = len(S)
    mp = [ [ 0 for _ in range(lenN)] for _ in range(lenN)]

    for n1 in range(lenN):
        for n2 in range(n1,lenN):
            mp[n1][n2] = min(arr[n1:n2+1])

    result = [0 for _ in range(lenP)]
    for i in range(lenP):
        result[i] = mp[P[i]][Q[i]]
    return result 
