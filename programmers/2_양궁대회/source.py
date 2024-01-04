from collections import deque

def calculate(aps, lis):
    a_cnt = 0
    l_cnt = 0 
    for i in range(11):
        if aps[i] == lis[i] and lis[i] == 0 :
            continue
        elif aps[i] >= lis[i] :
            a_cnt += (10-i)
        else:
            l_cnt += (10-i)
    return l_cnt - a_cnt

def solution(n, info):
    answer_val = 0
    answer = []
    li = [0 for _ in range(11)]    
    visited = []
    queue = deque([[n,0,li]]) # cnt, idx, list

    while queue:
        temp = queue.popleft()
        # print(temp)
        cnt = temp[0]
        idx = temp[1]
        li = temp[2] 
        if idx >10: continue
        if cnt == 0 :
            val = 0 #calculate(info, li)
            if answer_val < val:
                answer_val = val
                answer = li
        idx +=1 
        queue.append([cnt, idx, li])
        
        if idx == 10:
            li[idx] += cnt
            queue.append([0, idx, li])
        elif cnt >= info[idx]+1:            
            cnt -=  info[idx]+1
            li[idx] = info[idx]+1
            queue.append([cnt, idx, li])
        # break
    print(answer_val)
    print(answer)
    return answer
