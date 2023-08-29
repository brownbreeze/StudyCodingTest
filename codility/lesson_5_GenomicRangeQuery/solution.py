def solution(S, P, Q):
    # A1 C2 G3 T4
    # CA GCC TA 
    # P 2  Q 4  -> GCC 3,2  -> 2
    # P 5 Q 5.  -> T 4 -> 4
    # P 0 Q 6  -> 1
    dic = {'A':1, 'C':2, 'G':3, 'T':4}
    arr = [dic[s] for s in S]
    r_max = len(P)
    ret = [0 for _ in range(r_max)]
    for i in range(r_max):
        p = P[i]
        q = Q[i] +1
        ret[i] = min(arr[p:q])
        # print(p,q,arr[p:q])
    return ret 
