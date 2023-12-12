from collections import deque
def get_time(times, i):
    time_s = times[i][1]
    data =time_s.split(':')
    return int(data[0])*60 + int(data[1])

def solution(plans):
    answer = []
    left_time = 0
    left_name = ''
    waiting = [] # append, pop
    plans.sort(key = lambda x :x[1])
    qz = deque(plans) # leftpop
    t = -1 
    while True:
        if t > 100000: break
        t += 1 
    
        # 하던거 해 
        if left_name != '':
            left_time -= 1
            if left_time <= 0:
                answer.append(left_name)
                left_name = ''
        # 새로운 과제가 있으면 과제부터해 
        if len(qz) != 0 and get_time(qz, 0) <= t:
            if left_name != '':
                waiting.append([left_name, left_time])
            plan = qz.popleft()
            left_name = plan[0]
            left_time = int(plan[2])
            # print('<=', t, left_name, ' pop')
        elif left_name == '' and len(waiting) !=0 :
        # 하는거 없으면 밀린과제 갖고와
            val = waiting.pop()
            left_name = val[0]
            left_time = val[1]
        # if left_name != '' :
        #     print(t, left_name, left_time)
    return answer
