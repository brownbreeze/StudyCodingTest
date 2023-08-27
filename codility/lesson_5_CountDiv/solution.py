def solution(A, B, K):
    cnt = 0
    for i in range(A,B+1):
        if i == 0 : continue
        if i % K == 0 : 
            cnt +=1 
    return cnt
