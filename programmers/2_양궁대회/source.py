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
    max_pos = 0
    li = [0 for _ in range(11)]    
    visited = []
    queue = deque([[n,-1,li]]) # cnt, idx, list

    while queue:
        temp = queue.popleft()
        cnt = temp[0]
        idx = temp[1]
        li = temp[2].copy()
        if max_pos !=0 and max_pos <idx:
            break
        if cnt == 0 or idx == 10:
            print('cnt ', li)
            val = 0 #calculate(info, li)
            if max_pos == 0 :
                max_pos = idx 
            if answer_val < val:
                answer_val = val
                answer = li
            break
        
        idx +=1 
        queue.append([cnt, idx, li])
        if idx == 9:
            li[idx] += cnt
            queue.append([0, idx, li])
            li[idx] -= cnt
        elif cnt >= info[idx]+1:            
            cnt -=  info[idx]+1
            li[idx] = info[idx]+1
            queue.append([cnt, idx, li])
    return answer
