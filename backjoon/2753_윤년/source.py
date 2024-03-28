import sys


def solution(num):
    if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
        return 1
    return 0


input = sys.stdin.readline
t = int(input())
print(solution(t))
