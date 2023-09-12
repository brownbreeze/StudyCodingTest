def solution(A):
    cnt = 0
    len_a = len(A)

    for i in range(len_a):
        for j in range(i+1, len_a):
            a = i 
            b = j
            if a + A[a] >= b-A[b] :
                cnt +=1
            if cnt > 10000000:
                return -1 
    return cnt
