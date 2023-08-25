def solution(A):
    num = 1
    A.sort()
    if A[-1] < 0 :
        return 1
    for a in A:
        if a  < 0 : continue
        if a == num :
            continue 
        elif a == num+1:
            num = a 
        else : 
            return num + 1
    return num + 1
