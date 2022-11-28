# n이 소수인지 판정
def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def solution(n, k):
    answer = 0
    arr = list()    
    while True:
        arr.append(str(n % k)) 
        n = n // k
        if n == 0 : break
        if n < k :
            arr.append(str(n))
            break

    arr = arr[::-1]
    temp_str = ''.join(arr).split('0')
    temp_list = [int(st) if st != '' else 0 for st in temp_str]

    for t in temp_list:
        if isprime(t): answer += 1
    
    return answer
