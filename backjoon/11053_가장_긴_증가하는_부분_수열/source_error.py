# error
# 4
# 1 3 2 3
# 오답 2
# 정답 3(1,2,3)
import sys


def solution(num, arr):
    temp = [0 for _ in range(num)]
    t = 1
    temp[0] = arr[0]
    for i in range(1, len(arr)):
        if temp[i-1] < arr[i]:
            temp[i] = arr[i]
            t += 1
        else:
            temp[i] = temp[i-1]
    return t


input = sys.stdin.readline
t = int(input())
arr = input().split()
arr = [int(i) for i in arr]
print(solution(t, arr))
