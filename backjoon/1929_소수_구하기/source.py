import sys
import math
from itertools import permutations


def is_prime_number(x):
    if x == 2:
        return True
    elif x == 1:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(n1, n2):
    for i in range(n1, n2+1):
        if is_prime_number(i):
            print(i)


input = sys.stdin.readline
q = input().split()
solution(int(q[0]), int(q[1]))
