from  collections import Counter 

def get_leader(cnt, l):
    # print(cnt, l)
    val = cnt.most_common(1)[0][1] 
    if val > (l/2.0) : 
        return cnt.most_common(1)[0][0] 
    return -1

def solution(A):
    r = Counter(A)
    l = Counter()
    left_len = 0
    total_len = len(A)
    cnt = 0
    for a in A:
        if r[a]==0: break
        left_len+=1
        r[a]-=1
        l[a]+=1
        f = get_leader(r,total_len-left_len)
        s = get_leader(l,left_len)
        if f == s and f != -1 : 
            cnt += 1 
    return cnt
