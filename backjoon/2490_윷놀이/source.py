import sys


def solution(arr):
    c = arr.count(0)
    if 1 == c:
        return 'A'
    elif 2 == c:
        return 'B'
    elif 3 == c:
        return 'C'
    elif 4 == c:
        return 'D'
    else:
        return 'E'


while True:
    try:
        arr = list(map(int, input().split()))
    except:
        break
    print(solution(arr))
