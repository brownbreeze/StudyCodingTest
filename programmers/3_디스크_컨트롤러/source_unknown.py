from collections import deque
def solution(jobs):
    answer = 0
    current = 0
    jobs_len = len(jobs)
    total_time = sum([job[1] for job in jobs])
    jobs.sort()
    deq = deque()
    deq.extend(jobs)
    while len(deq) > 0 :
        temp = [job for job in deq if job[0] <= current]
        if len(temp) == 0 :
            current += 1
            continue
        elif len(temp) == 1 :
            answer += current - temp[0][0] if  current - temp[0][0] > 0 else 0 
            current += temp[0][1]
            deq.remove(temp[0])
            continue
        temp = sorted(temp, key=lambda x:  x[1])
        #print(current, temp)
        answer += current - temp[0][0] if  current - temp[0][0] > 0 else 0 
        current += temp[0][1]
        deq.remove(temp[0])
        
    return (answer + total_time) // jobs_len
