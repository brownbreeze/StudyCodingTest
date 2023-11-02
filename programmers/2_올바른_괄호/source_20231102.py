def solution(s):
    num = 0
    for g in s:
        if g == '(':
            num += 1
        else:
            num -=1
        if num < 0 :
            return False
    if num != 0 :
        return False
    return True
