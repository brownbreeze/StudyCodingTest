def del_zero(li, n):
    while True:
        if len(li) == 0 : break
        if li[-1]==0:
            li.pop()
            continue
        elif n==0:
            break
        elif li[-1] <= n:
            n -= li[-1]
            li.pop()
        else:# li[-1] > n:
            li[-1]-= n
            break
    return li 

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliveries = del_zero(deliveries, 0)
    pickups = del_zero(pickups, 0)
    while True:
        pos = max(len(deliveries), len(pickups))
        if pos == 0:
            break
        deliveries = del_zero(deliveries, cap)   
        pickups = del_zero(pickups, cap)        
        # print(pos)
        # print(deliveries, pickups)
        answer += (pos*2)
    return answer
