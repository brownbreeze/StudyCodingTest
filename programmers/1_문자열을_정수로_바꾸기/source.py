def solution(s):
    if s[0] == '-' or s[0] == '+':
        number = int(s[1:])
        if s[0] == '-':
            return number * -1
    return int(s)
