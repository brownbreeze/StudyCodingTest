import sys


def solution(n, m):
    answer = []

    i = 0
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            break
    answer.append(i)

    i = 0
    for i in range(max(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            break
    answer.append(i)

    print(answer[0])
    print(answer[1])


input = sys.stdin.readline
q = input().split()
solution(int(q[0]), int(q[1]))
