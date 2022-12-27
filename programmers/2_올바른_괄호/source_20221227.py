def solution(s):
    arr = []
    open_gualho, close_gualho = '(', ')'
    for i in range(len(s)):
        #print(s[i])
        if len(arr)==0:
            if s[i] == open_gualho :
                arr.append(s[i])
            else :
                return False
        else:
            if s[i] == open_gualho:
                arr.append(s[i])
            elif arr[-1] == open_gualho:
                arr.pop()
            else:
                return False
    if len(arr) != 0 :
        return False
    return True
