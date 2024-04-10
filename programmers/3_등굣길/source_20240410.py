def solution(m, n, puddles):
    ma = [[0 for _ in range(m)] for _ in range(n)]

    for puddle in puddles:
        ma[puddle[1]-1][puddle[0]-1] = -1

    for y in range(n):
        for x in range(m):
            if ma[y][x] == -1:
                continue
            if (x, y) == (0, 0):
                continue
            if (x, y) == (1, 0) or (x, y) == (0, 1):
                ma[y][x] = 1
                continue

            if y != 0 and ma[y-1][x] != -1:
                ma[y][x] += ma[y-1][x] % 1000000007
            if x != 0 and ma[y][x-1] != -1:
                ma[y][x] += ma[y][x-1] % 1000000007

    return ma[-1][-1] % 1000000007
