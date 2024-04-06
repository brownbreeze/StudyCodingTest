import sys


def solution(arr):
    arr.sort()
    if arr[0] == arr[1] and arr[1] == arr[2]:
        return 10000+arr[1]*1000
    elif arr[0] != arr[1] and arr[1] != arr[2]:
        return arr[2]*100
    return arr[1]*100 + 1000


input = sys.stdin.readline
arr = list(map(int, input().split()))
print(solution(arr))
