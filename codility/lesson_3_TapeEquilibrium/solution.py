def solution(A):
    f = A[0]
    s = sum(A)-A[0]
    lena = len(A)
    tmp = sum(A)
    if lena == 2:
        return tmp
    for i in range(1,lena):
        if tmp < abs(f-s):
            return tmp 
        tmp = abs(f-s)
        f += A[i]
        s -= A[i]
    if tmp < abs(f-s):
        return tmp
    return abs(f-s)
