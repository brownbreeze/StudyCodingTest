def solution(S):
    cnt = 0
    for s in S: 
        if s == '(':
            cnt +=1
        elif cnt == 0:
            return 0
        else : 
            cnt -= 1
    if cnt == 0 :
        return 1
    return 0
