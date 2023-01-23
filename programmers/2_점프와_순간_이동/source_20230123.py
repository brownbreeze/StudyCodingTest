def solution(n):
    answer = 0
    while True:
        if n == 1:
            answer +=1
            break
        if n % 2== 0:
            n /= 2
            continue
        n -= 1 
        answer +=1 
        
    return answer
