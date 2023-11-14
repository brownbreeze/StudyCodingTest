def solution(babbling):
    icando = ["aya", "ye", "woo", "ma"]
    answer = 0
    for ba in babbling:
        temp = ba
        p = 0 
        t_l = len(temp)
        prev = '-'
        while True:
            if p >= t_l:break
            for i in range(4):
                if t_l < p + len(icando[i]): continue
                if icando[i] == prev : continue
                # print(ba[p:p+len(icando[i])], icando[i])
                if ba[p:p+len(icando[i])] == icando[i]:
                    p += len(icando[i])
                    prev = icando[i]
                    break
            else:
                break
        # print(p, ba, (p==t_l))
        # print()
        if p == t_l:
            answer+=1
    return answer
