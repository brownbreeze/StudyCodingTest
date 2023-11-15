def solution(strings, n):
    strings.sort(key=lambda x : (x[n], x), reverse=False)
    return strings
