import sys
from itertools import combinations


def solution(arr):
    for ar in combinations(arr, 7):
        if sum(ar) == 100:
            arr = sorted(list(ar))
            for i in arr:
                print(i)
            break


input = sys.stdin.readline
arr = list()
for i in range(9):
    arr.append(int(input()))
solution(arr)
