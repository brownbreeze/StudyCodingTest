def solution(A):
    A.sort()
    prev = -1000001
    cnt = 0
    for a in A:
        if prev != a:
            prev = a
            cnt +=1
    return cnt
