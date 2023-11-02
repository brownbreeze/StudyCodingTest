from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    cur_weight = 0 
    bridge = deque()
    trucks = deque(truck_weights)
    while True:
        # print(time, trucks, bridge)
        if len(trucks) == 0 and len(bridge) == 0 : break
        time +=1
        if len(bridge) !=0 and time - bridge[0][1] >= bridge_length : 
            w, t = bridge.popleft()
            cur_weight -= w
        
        if len(trucks) <= 0 : continue 
        if trucks[0] + cur_weight > weight: continue
        w = trucks.popleft()
        bridge.append([w, time])
        cur_weight += w
    return time
