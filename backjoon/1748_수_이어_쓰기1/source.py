# pypy
import sys
import math


def solution(num):
    i = 1
    j = 10
    t = 1
    result = 0
    while i <= num:
        if i >= j:
            j *= 10
            t += 1
        i += 1
        result += t
    return result


input = sys.stdin.readline
t = int(input())
print(solution(t))
