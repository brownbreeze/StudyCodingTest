from collections import deque 

def solution(N, road, K):
    answer = 0
    stack = deque()
    result = [500000 for _ in range(N)]
    result[0] = 0
    
    for r in road:
        f = min(r[0], r[1])
        t = max(r[1], r[0])
        if f == 1:
            stack.append([[f-1,t-1],r[2]]) # list(이미 방문), 거리값
            
    while True:
        if len(stack) == 0 : break
        gone_list, value = stack.popleft()
        # print(gone_list, value)
        last_gone = gone_list[-1]
        if value < result[last_gone] :
            result[last_gone] = value  
        else:
            continue
        for r in road:
            if r[0] -1 == last_gone :
                if r[1] -1 in gone_list : continue 
                gone_list.append(r[1]-1)
                stack.append([gone_list.copy(), r[2]+value])
                gone_list.pop()
            if r[1] -1 == last_gone :
                if r[0] -1 in gone_list : continue 
                gone_list.append(r[0]-1)
                stack.append([gone_list.copy(), r[2]+value])
                gone_list.pop()
    # print()
    # print(result)
    for i in result:
        if i <= K:
            answer += 1
    return answer
