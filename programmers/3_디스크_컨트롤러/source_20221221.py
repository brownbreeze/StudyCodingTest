from collections import deque
def solution(jobs):
    answer = 0
    now = 0
    total_time = sum([job[1] for job in jobs])
    deq = deque()
    deq.extend(jobs)
    
    while len(deq) > 0:
        temp = [job for job in deq if job[0] <= now]
        if len(temp) == 0 :
            now += 1
            continue
        elif len(temp) != 1:
            temp = sorted(temp, key=lambda x: x[1])
        answer += now - temp[0][0] if now - temp[0][0] > 0 else 0
        now += temp[0][1]
        deq.remove(temp[0])
    return ( answer + total_time ) // len(jobs)
