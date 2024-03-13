from sys import stdin


def solution(num):

    one = '1'
    i = 0
    j = 0
    while True:
        i *= 10
        i += 1
        j += 1
        if i % num == 0:
            return j


while True:
    try:
        N = int(stdin.readline().rstrip())
    except:
        break
    print(solution(N))
