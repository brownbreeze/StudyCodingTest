def solution(A):
    B = A.copy()
    B.sort()
    if len(A)==0: return -1
    dom = B[len(B)//2] if A.count(B[len(B)//2-1]) < A.count(B[len(B)//2]) else B[len(B)//2-1]
    # print(B.count(dom), len(B)/2.0)
    if B.count(dom) > len(B)/2.0:
        for i in range(len(A)):
            if A[i]==dom:
                return i
    return -1
