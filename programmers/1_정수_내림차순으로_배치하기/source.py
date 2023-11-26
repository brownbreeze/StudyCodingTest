def solution(n):
    n = str(n)
    n = sorted(n, reverse=True)
    n = ''.join(n)
    return int(n)
