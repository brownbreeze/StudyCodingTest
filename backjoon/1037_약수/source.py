import sys


def gongbaesoo(a, b):
    i = 0
    for i in range(max(a, b), a*b+1):
        if i % a == 0 and i % b == 0:
            break
    return i


def solution(c, num):
    if c == 1:
        return num[0]*2
    result = 1
    for n in num:
        result = gongbaesoo(result, n)
    if max(num) == result:
        return result*2
    return result


input = sys.stdin.readline
t = int(input())
arr = list(map(int, input().split()))
# print(arr)
print(solution(t, arr))
