import sys


def solution(num):
    return str(bin(num)).count('1')


input = sys.stdin.readline
t = int(input())
print(solution(t))

# n = int(sys.stdin.readline())
# while n != 0:
#     solution(n)
#     n = int(sys.stdin.readline())
