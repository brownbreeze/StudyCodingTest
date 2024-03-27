import sys
import itertools


def solution(num, arr):
    result = 0
    arr.sort()
    num = len(arr)
    for i in range(num):
        for j in range(i+1, num):
            v = arr[i] ^ arr[j]
            result = max(v, result)
    return result


input = sys.stdin.readline
n = int(input())
ar = list(map(int, input().split()))
print(solution(n, ar))
