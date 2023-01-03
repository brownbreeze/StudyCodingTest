def get_one_time(n):
    cnt = 0
    while True:
        if n==0 :break
        if n%2==1: cnt +=1
        n //= 2
    return cnt        
    
def solution(n):
    num = get_one_time(n)
    while True:
        n+=1
        if num == get_one_time(n):
            return n
    return -1
