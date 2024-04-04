import sys


def solution(arr):
    if len(arr) == 0:
        print(-1)
    else:
        print(sum(arr))
        arr.sort()
        print(arr[0])


arr = []
input = sys.stdin.readline
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        arr.append(n)
solution(arr)
