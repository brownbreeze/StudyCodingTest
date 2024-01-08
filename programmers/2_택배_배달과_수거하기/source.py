def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # deliver, pickup
    totals = [[a,b] for a,b in zip(deliveries, pickups)]
    
    while True:
        pos = n-1
        for a,b in totals[::-1]:
            if a!=0 or b!=0:
                break
            pos-=1
        else:
            break
        # i 는 position
        c = cap
        for i in range(n):
            if c == 0 : break
            if totals[n-i-1][0] > c:
                totals[n-i-1][0] -= c
                c = 0
            elif totals[n-i-1][0] > 0:
                c -= totals[n-i-1][0]
                totals[n-i-1][0] = 0
        c = cap
        for i in range(n):
            if c == 0 : break
            if totals[n-i-1][1] > c:
                totals[n-i-1][1] -= c
                c = 0
            elif totals[n-i-1][1] > 0:
                c -= totals[n-i-1][1]
                totals[n-i-1][1] = 0
        # print(pos)
        pos +=1
        answer += (pos*2)
        
    return answer
