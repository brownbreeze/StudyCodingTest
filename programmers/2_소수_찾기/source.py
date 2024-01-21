import math
from itertools import permutations

# 소수 판별 함수
def is_prime_number(x):
    if x<=2: return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(numbers):
    answer = 0
    f = 0

    values = []
    for i in range(1,len(numbers)+1):
        datas = list(permutations(list(numbers), i))
        # values.append(datas)
        for data in datas:
            values.append(int(''.join(list(data))))
    values = list(set(values))
    # print(values)
    
    for value in values:
        if is_prime_number(value):
            answer += 1
    
    return answer
