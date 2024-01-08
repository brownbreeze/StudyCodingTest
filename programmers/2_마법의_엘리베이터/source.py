from collections import deque 

def get_vals(num):
    val = [int(i) for i in str(num)]
    val = val[::-1]
    i = 0
    for i in range(len(val)):
        if val[i] != 0 :
            break
    
    return [(10-val[i]), pow(10, i) *  (10-val[i])+ num], [val[i], (pow(10, i) * val[i]  * -1) + num]
    
def solution(storey):
    answer = 100000000
    lia, lib = get_vals(storey)
    dq = deque() 
    dq.append(lia)
    dq.append(lib)
    
    while True:
        if len(dq)==0: break
        cnt, num = dq.popleft()
        if cnt >= answer :
            continue
        if num == 0:
            answer = min(answer, cnt)
        lia, lib = get_vals(num)
        dq.append([lia[0]+cnt, lia[1]])
        dq.append([lib[0]+cnt, lib[1]])
        
    return answer
