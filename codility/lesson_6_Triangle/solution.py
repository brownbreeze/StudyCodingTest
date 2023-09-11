def solution(A):
    A.sort()
    
    for i in range(len(A)-2):
        if A[i] < 0 : continue 
        if A[i] + A[i+1] <= A[i+2] : continue
        if A[i] + A[i+2] <= A[i+1] : continue
        if A[i+2] + A[i+1] <= A[i] : continue
        return 1
    else: 
        return 0
    return 0
