
from collections import deque
def go_pos(fr, to, n, fares):
    s = fr
    stack = deque()
    result = [100000*201 for _ in range(n)]
    if fr == to: 
        return 0
    for fare in fares :
        f = fare[0]
        t = fare[1]
        if f == s:
            stack.append([[f-1,t-1], fare[2]])
        elif t == s:
            stack.append([[t-1,f-1], fare[2]])
    while True:
        if len(stack) == 0: break
        gone_list, value = stack.popleft()
        last_gone = gone_list[-1]
        if value < result[last_gone]:
            result[last_gone] = value
        else:
            continue
        for fare in fares:
            if fare[0]-1 == last_gone:
                if fare[1]-1 in gone_list : continue
                gone_list.append(fare[1]-1)
                stack.append([gone_list.copy(), fare[2]+value])
                gone_list.pop()
            if fare[1]-1 == last_gone:
                if fare[0]-1 in gone_list : continue
                gone_list.append(fare[0]-1)
                stack.append([gone_list.copy(), fare[2]+value])
                gone_list.pop()
    # print('>', fr, to, result[to-1], '(', result)
    return result[to-1]
    
def solution(n, s, a, b, fares):
    answer = -1
    stack = deque()
    result = [100000*201 for _ in range(n)]
    for fare in fares :
        f = fare[0]
        t = fare[1]
        if f == s:
            stack.append([[f-1,t-1], fare[2]])
        elif t == s:
            stack.append([[t-1,f-1], fare[2]])
    while True:
        if len(stack) == 0: break
        gone_list, value = stack.popleft()
        last_gone = gone_list[-1]
        if value < result[last_gone]:
            result[last_gone] = value
        else:
            continue
        for fare in fares:
            if fare[0]-1 == last_gone:
                if fare[1]-1 in gone_list : continue
                gone_list.append(fare[1]-1)
                stack.append([gone_list.copy(), fare[2]+value])
                gone_list.pop()
            if fare[1]-1 == last_gone:
                if fare[0]-1 in gone_list : continue
                gone_list.append(fare[0]-1)
                stack.append([gone_list.copy(), fare[2]+value])
                gone_list.pop()
    # print(result)
    # print()
    answer = go_pos(s,a, n, fares)
    answer += go_pos(s,b, n, fares)
    # print()
    for i in range(n):
        if i == s-1: continue
        # print('start::', result[i])
        temp = result[i]
        temp += go_pos(i+1, a, n, fares)
        temp += go_pos(i+1, b, n, fares)
        if answer == -1:
            answer = temp
        else:
            answer = min(answer, temp)
        # print(answer)
    return answer
