import math
def isprime(num):
    if num < 2: return 0
    max_c = (int)(math.sqrt(num))
    for i in range(2,max_c+1):
        if num % i == 0:
            return 0
    return 1
    
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
    temp_list.sort()

    for t in temp_list:
        answer += isprime(t)
    
    return answer
