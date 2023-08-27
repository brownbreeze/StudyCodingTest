def solution(A, B, K):
    b = B//K
    a = (A-1)//K if A > 0 else 0
    return b-a
