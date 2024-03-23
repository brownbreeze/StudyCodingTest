import sys


map = list()
result = 0
t = 0


def check(y, x, value, d):
    v = 1
    global t
    if d == 1:
        for i in range(y+1, t):
            if value == map[i][x]:
                v += 1
            else:
                break
        for i in range(y-1, -1, -1):
            if value == map[i][x]:
                v += 1
            else:
                break
    else:
        for i in range(x+1, t):
            if value == map[y][i]:
                v += 1
            else:
                break
        for i in range(x-1, -1, -1):
            if value == map[y][i]:
                v += 1
            else:
                break
    global result
    if result < v:
        result = v


def solution(num):
    for y in range(num):
        for x in range(num):
            if x + 1 < num:
                check(y, x, map[y][x+1], 1)
                check(y, x+1, map[y][x], 1)
            if y + 1 < num:
                check(y, x, map[y+1][x], 0)
                check(y+1, x, map[y][x], 0)
            break
        break


input = sys.stdin.readline
t = int(input())
for i in range(t):
    map.append(input())
solution(t)
print(result)
