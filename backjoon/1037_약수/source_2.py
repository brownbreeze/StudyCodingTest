import sys


def solution(c, num):
    mxnum = max(num)
    for i in range(2, 1000001):
        for n in num:
            if i % n != 0:
                break
        else:
            if mxnum == i:
                continue
            return i


input = sys.stdin.readline
t = int(input())
arr = list(map(int, input().split()))
# print(arr)
print(solution(t, arr))
