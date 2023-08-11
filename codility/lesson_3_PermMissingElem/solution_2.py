def solution(A):
    if len(A) == 0:
        result = 1
    else : 
	result = sum(range(1,len(A)+2)) - sum(A)
    return result 
