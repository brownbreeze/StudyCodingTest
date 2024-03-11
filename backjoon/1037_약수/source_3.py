import sys


def solution(c, num):
    return min(num)*max(num)


input = sys.stdin.readline
t = int(input())
arr = list(map(int, input().split()))
print(solution(t, arr))

