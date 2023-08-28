def solution(A, B, K):
    b = B//K if B > 0 else 1
    a = (A-1)//K if A > 0 else 0
    if A==0 and B== 0 :
        return 1
    if A == 0:
        return b-a + 1 if b!=a else 1 
    else :
        return b-a if b!=a else 0
