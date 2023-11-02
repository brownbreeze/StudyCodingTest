from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0 
    cur_weight = 0 
    
    waits = deque()
    waits.extend(truck_weights)
    
    run_trucks = deque()
    
    #n = 0 
    while True:
        #n+=1
        if len(waits) == 0 and len(run_trucks)==0 : 
            break
        time += 1
            
        # 차가 나간다
        if len(run_trucks) > 0 and time - run_trucks[0][1] == bridge_length:
            cur_weight -= run_trucks[0][0]    
            run_trucks.popleft()
            
        # 차가 들어온다 
        if len(waits) > 0 and  cur_weight + waits[0] <= weight:
            # 지나간다
            cur_weight += waits[0]
            run_trucks.append([waits.popleft(),time])

            
    return time
