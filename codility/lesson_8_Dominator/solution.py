def solution(A):
    B = A.copy()
    B.sort()
    dom = B[len(B)//2]
    if B.count(dom) < int(len(B)//2):
        return -1
    for i in range(len(A)):
        if A[i]==dom:
            return i
    return -1
