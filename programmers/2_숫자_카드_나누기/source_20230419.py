def go(A,B):
    max_num = max(A)
    min_num = min(A)
    i = 1
    while True:
        i+=1
        if max_num%i !=0:
            continue
        if max_num//2 < i:
            break
        num = max_num//i
        for a in A:
            if a%num !=0: break
        else:
            if num in B: 
                continue
            else:
                return num 
    return 0

def solution(arrayA, arrayB):
    answer = 0
    
    a = go(arrayA, arrayB)
    
    return a
