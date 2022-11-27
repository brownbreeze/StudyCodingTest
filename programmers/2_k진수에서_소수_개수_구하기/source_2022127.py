
import math
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

    if len(temp_list) == 0 or temp_list[-1] < 1 :
        return 0
    
    max_li = temp_list[-1]+1
    check_prime = [True for _ in range(max_li)]
    i = 2
    m = (int)(math.sqrt(max_li))
    for i in range(2, m+1):
        if check_prime[i] :
            for j in range(i+i, max_li, i):
                check_prime[j] = False
    prim_list = [i for i in range(2,max_li) if check_prime[i]==True]
    
    for t in temp_list:
        if t in prim_list: answer += 1 
    
    return answer
