import sys


def solution(AL, A, ML, M):
    # print(A, M)
    d = dict()
    for a in A:
        d[a] = 1

    for m in M:
        if m in d:
            print(1)
        else:
            print(0)


input = sys.stdin.readline
AL = int(input())
A = list(map(int, input().split()))
ML = int(input())
M = list(map(int, input().split()))

solution(AL, A, ML, M)

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
