def correct_p(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else :
            cnt -=1
        if cnt <0 :
            return False
    if cnt == 0 :
        return True
    return False 

def go_find(p):
    if len(p) == 0 or correct_p(p) : 
        return p   
    if p==')(':
        return '()'
    
    idx = 0 
    for i in range(2,len(p),2):
        half = p[:i].count(')')
        if half == i//2: # 균형
            idx = i
            break
    else:
        idx = len(p)
    
    if correct_p(p[:idx]):
        return p[:idx]+go_find(p[idx:]) #v 수행

    temp = '('+go_find(p[idx:])+')' # 4-1~4-3
    for i in p[1:idx-1]:
        if i=='(':
            temp+=')'
        else:   
            temp+='('
    return temp

def solution(p):
    answer = go_find(p)
    return answer
