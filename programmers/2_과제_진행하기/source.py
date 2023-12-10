from collections import deque
def get_time(times, i):
    time_s = times[i][1]
    data =time_s.split(':')
    return int(data[0])*60 + int(data[1])

def solution(plans):
    answer = []
    qz = deque(plans) # leftpop
    left_time = 0
    left_name = ''
    waiting = [] # append, pop
    
    t = -1 
    while True:
        if t > 25*60 + 60: break
        t += 1 
        
        # 새로운 과제가 있으면 과제부터해 
        if len(qz) != 0 and get_time(qz, 0) <= t:
            if left_name != '':
                waiting.append([left_name, left_time])
            plan = qz.popleft()
            left_name = plan[0]
            left_time = int(plan[2])
        # 하던거 해 
        if left_name != '':
            left_time -= 1
            if left_time <= 0:
                answer.append(left_name)
                left_name = ''
        # 하는거 없으면 밀린과제 갖고와
        if left_name == '' and len(waiting) !=0 :
            val = waiting.pop()
            left_name = val[0]
            left_time = val[1]
                
    return answer
