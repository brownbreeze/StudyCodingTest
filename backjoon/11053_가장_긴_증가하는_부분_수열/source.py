# error
# 4
# 1 3 2 3
# 오답 2
# 정답 3(1,2,3)
import sys


def solution(num, arr):
    maxv = 0
    temp = [0 for _ in range(num)]
    t = 1
    for i in range(1, len(arr)):
        minv = 0
        for j in range(i):
            if arr[i] > arr[j] and minv < temp[j]:
                minv = arr[j]
        temp[i] = minv + 1
        if maxv < arr[i]:
            t += 1
            maxv = arr[i]
    return t


input = sys.stdin.readline
t = int(input())
arr = input().split()
arr = [int(i) for i in arr]
print(solution(t, arr))
