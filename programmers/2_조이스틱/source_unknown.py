def solution(name):
    answer = 0
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_len = len(alpha)
    # print(alpha_len)
    pos = 0
    for ch in name:
        to_go = alpha.index(ch)
        # print(answer,")",pos,"->", to_go)
        a,b = (pos,to_go) if pos > to_go else (to_go,pos) # a > b
        if to_go == 0 or to_go == alpha_len-1 : 
            answer += 1 
        else:
            answer += min(a-b, alpha_len-b+1+a, 1+a)
    return answer
