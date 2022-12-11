from collections import deque

def solution(queue1, queue2):
    answer = 0
    max_count = len(queue1)+len(queue2)
    que1, que2 = deque(queue1), deque(queue2)
    sum_q1, sum_q2 = sum(que1), sum(que2)
    while True:
        if answer >= 1.5*max_count: return -1
        if sum_q1 == sum_q2: break
        elif sum_q1 > sum_q2:
            sum_q1 -= que1[0]
            sum_q2 += que1[0]
            que2.append(que1.popleft())
        else:
            sum_q2 -= que2[0]
            sum_q1 += que2[0]
            que1.append(que2.popleft())
        answer += 1
    return answer
