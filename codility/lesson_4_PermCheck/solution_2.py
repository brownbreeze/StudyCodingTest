def solution(A):
    A.sort()
    al = len(A)
    for i in range(0, al):
        if i+1 == A[i]: 
            continue
        return 0
    return 1
