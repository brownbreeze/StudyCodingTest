def solution(babbling):
    answer = 0
    check_list = ['aya', 'ye', 'woo', 'ma']
    for ba in babbling:
        l = len(ba)
        i = 0
        flag = 0
        while True:
            flag = 0
            if i >= l : break
            for ch in check_list:
                if flag == 1: break
                if len(ch) > l-i: continue
                if ba[i:i+len(ch)] == ch:
                    i = i+len(ch)
                    flag = 1
            else : 
                if flag == 0: break
        if i == l:
            answer +=1 
            
    return answer
