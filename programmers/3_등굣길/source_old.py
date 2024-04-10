def solution(m, n, puddles):
    reg = [[0]*m for i in range(n)]

    for y in range(n):
        for x in range(m):
            if (x, y) == (0, 0) or [x+1, y+1] in puddles:
                continue
            elif (x, y) == (1, 0) or (x, y) == (0, 1):
                reg[y][x] = 1
                continue

            if x > 0:
                reg[y][x] += reg[y][x-1]
            if y > 0:
                reg[y][x] += reg[y-1][x]

    return reg[n-1][m-1] % 1000000007
