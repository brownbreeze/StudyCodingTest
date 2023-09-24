def get_leader(B):
    B.sort()
    if len(B)==0: return -1
    dom = B[len(B)//2] if B.count(B[len(B)//2-1]) < B.count(B[len(B)//2]) else B[len(B)//2-1]
    if B.count(dom) > len(B)/2.0:
        return dom
    return -1

def solution(A):
    cnt = 0
    for i in range(1,len(A)):
        f = get_leader(A[:i])
        s = get_leader(A[i:])
        if f == s and f != -1 : 
            cnt += 1 
    return cnt 

