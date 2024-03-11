import sys


def solution(c):
    result = [0 for _ in range(1000001)]
    for i in range(1, c+1):
        j = 1
        while True:
            if i * j > c:
                break
            result[i*j] += i
            j += 1
    # print(result[:10])
    return sum(result[:c+1])


input = sys.stdin.readline
t = int(input())
print(solution(t))
