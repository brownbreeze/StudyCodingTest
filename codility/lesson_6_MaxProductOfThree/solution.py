def solution(A):
    A.sort()
    # 
    if A[-1] < 0 : # 모두 음수일 경우 
        return 0 
    if A[0] > 0 : # 모두가 양수
        return A[-1]* A[-2]* A[-3]
    
    if A[1] <= 0 :
        top3 =  A[-1]*A[-2]*A[-3]
        top1_under2 = A[-1]*A[0]*A[1]
        if top3> top1_under2:
            return top3
        else : 
            return top1_under2
    else : 
        return A[-1]* A[-2]* A[-3]
