def solution(n):
    l = 0
    r = 1
    for i in range(n-1):
        t = l
        l = r
        r = (t+l)%1234567
    return r
