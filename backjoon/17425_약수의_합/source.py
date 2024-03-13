import sys

total = dict()


def solution(c):
    result = 0
    for i in range(1, c+1):
        result += (c//i) * i
    return result


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    print(solution(int(input())))
