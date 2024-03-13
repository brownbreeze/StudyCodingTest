import sys


def solution(c):
    result = 0
    for i in range(1, c+1):
        result += (c//i) * i
    return result


input = sys.stdin.readline
t = int(input())
print(solution(t))
