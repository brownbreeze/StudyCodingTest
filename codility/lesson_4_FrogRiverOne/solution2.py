def solution(X, A):
    arr = [1 for _ in range(0,1000001)]
    tmp = 0
    i = 0
    for a in A:
        if arr[a]==1 and a<=X:
            arr[a] = 0
            tmp += 1
        if tmp == X:
            return i
        i += 1
    return -1
