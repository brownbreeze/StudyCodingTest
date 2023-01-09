from collections import deque
def solution(order):
    answer = 0
    order = deque(order)
    ord_len = len(order)
    bozo = []
    cur = 0
    find = order.popleft()
    
    while True:
        cur += 1
        if find == cur: 
            answer +=1
            if len(order)==0 : break
            find = order.popleft()
        elif len(bozo)>0 and find == bozo[-1]:
            bozo.pop()
            answer +=1            
            if len(order)==0 : break
            find = order.popleft()
            cur -= 1
        elif cur > find or cur > ord_len:
            break
        else:
            bozo.append(cur)
    return answer
