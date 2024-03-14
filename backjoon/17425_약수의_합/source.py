import sys

total = dict()


def maketotal(c):
    for i in range(1, c+1):
        if i in total:
            total[i] += (c//i) * i
        else:
            total[i] = (c//i) * i


def solution(c):
    return total[c]


input = sys.stdin.readline
t = int(input())
maketotal(1000000)
for _ in range(t):
    print(solution(int(input())))
