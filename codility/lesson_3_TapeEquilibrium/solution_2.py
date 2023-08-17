def solution(A):
    f = A[0]
    s = sum(A)-A[0]
    lena = len(A)
    tmp = abs(f-s)
    if lena == 2:
        return tmp
    for i in range(1,lena):
        if tmp > abs(f-s):
            tmp = abs(f-s)
        f += A[i]
        s -= A[i]
    return tmp
