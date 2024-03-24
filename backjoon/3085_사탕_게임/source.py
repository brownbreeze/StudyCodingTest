import sys


map = list()
result = 0
t = 0


def check(y, x):
    global t
    global result
    v = 1
    for i in range(y+1, t):
        if map[y][x] == map[i][x]:
            v += 1
        else:
            break
    for i in range(y-1, -1, -1):
        if map[y][x] == map[i][x]:
            v += 1
        else:
            break
    result = max(result, v)

    v = 1
    for i in range(x+1, t):
        if map[y][x] == map[y][i]:
            v += 1
        else:
            break
    for i in range(x-1, -1, -1):
        if map[y][x] == map[y][i]:
            v += 1
        else:
            break
    result = max(result, v)


def solution(num):
    for y in range(0, num):
        for x in range(0, num):
            if x + 1 < num:
                # print(y, x, x+1, map[y][x], map[y][x+1], '좌우')
                tmp = map[y][x+1]
                map[y][x+1] = map[y][x]
                map[y][x] = tmp

                check(y, x)
                check(y, x+1)

                tmp = map[y][x+1]
                map[y][x+1] = map[y][x]
                map[y][x] = tmp

            if y + 1 < num:
                # print(y, x, y+1, map[y][x])
                tmp = map[y+1][x]
                map[y+1][x] = map[y][x]
                map[y][x] = tmp

                check(y, x)
                check(y+1, x)

                tmp = map[y+1][x]
                map[y+1][x] = map[y][x]
                map[y][x] = tmp


input = sys.stdin.readline
t = int(input())
for i in range(t):
    map.append(list(input()))
solution(t)
print(result)
