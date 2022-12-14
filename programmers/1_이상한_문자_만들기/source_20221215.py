def solution(s):
    chars = list(s)
    idx = -1
    for i in range(len(chars)):
        idx += 1
        if chars[i] == ' ':
            idx = -1
        chars[i] = chars[i].upper() if idx%2==0 else chars[i].lower()
    return ''.join(chars)
