import string
tmp = string.digits+string.ascii_uppercase
def func(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return func(q, base) + tmp[r]
    
def solution(n, t, m, p):
    answer = ''
    i = 0
    pos = 1
    answer_len = 0
    if m == p :
        p = 0 
    while True:
        next_value = func(i, n)
        i+=1
        # print(f'start next_value = {next_value}')
        for value in next_value:
            # print(value)
            if pos % m == p:
                answer+=value
                answer_len+=1
            pos+=1
            if answer_len == t: break
        if answer_len==t: break
    return answer
