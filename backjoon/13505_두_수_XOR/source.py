import sys


def solution(num, arr):
    arr = set(arr)
    arr = list(arr)
    if len(arr) <= 1:
        return 0
    num = len(arr)
    result = 0
    arr.sort()
    for i in range(num//2+1):
        for j in range(num-1, i, -1):
            if result == 0:
                result = arr[i] ^ arr[j]
            elif result < arr[i] ^ arr[j]:
                return arr[i] ^ arr[j]
    return result


input = sys.stdin.readline
n = int(input())
ar = list(map(int, input().split()))
print(solution(n, ar))
