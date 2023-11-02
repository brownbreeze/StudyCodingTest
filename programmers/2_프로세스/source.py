from collections import deque
def solution(priorities, location):
    answer = 0 
    pro_que = deque(priorities)
    priorities.sort()
    while True:
        if len(pro_que) == 0 : break
        if pro_que[0] == priorities[-1]:
            priorities.pop()
            pro_que.popleft()
            answer += 1
            if location == 0:
                return answer
            location -= 1        
        else:
            if location == 0:
                location = len(pro_que)-1
            else:
                location -= 1
            temp = pro_que.popleft()
            pro_que.append(temp)
        # print(pro_que, location, answer)
    return -1
