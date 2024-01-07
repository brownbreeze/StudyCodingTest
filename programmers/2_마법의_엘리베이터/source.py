from collections import deque 

def solution(storey):
    answer = 0
    check = [0 for _ in range(100000000)]
    # BFS
    arr = deque()
    vals = [-10000000,-1000000,-100000,-10000,-1000,-100,-10,-1,1,10,100,1000,10000,100000,1000000, 10000000]
    
    for val in vals:
        if storey+val >= 0 and pow(10, len(str(storey))) > storey+val:
            arr.append([1, storey+val])
            check[storey+val] = 1
    
    while True:
        if len(arr)== 0 :
            break
        temp = arr.popleft()
        idx = temp[0]
        cur = temp[1]
        if cur == 0: return idx
    
        for val in vals:
            t = cur+val
            if t >= 0 and t in range(100000000) and check[cur+val]==0 and  pow(10, len(str(storey))) > t:
                check[cur+val] = 1
                arr.append([idx+1, cur+val])
        if idx >= 20: break
    return answer
