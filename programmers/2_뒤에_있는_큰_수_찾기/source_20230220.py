from collections import deque

def solution(numbers):
    answer = deque()
    que = deque()
    num_len = len(numbers)
    for i in range(num_len-1,-1,-1):
        if len(que) == 0 :
            answer.append(-1)
            que.append(numbers[i])
            continue
        if numbers[i] >= que[-1]:
            answer.appendleft(-1)
            que = deque()
            que.append(numbers[i])
        else:
            while True:
                if len(que) == 0 : break
                if numbers[i] < que[0]:
                    answer.appendleft(que[0])
                    que.appendleft(numbers[i])
                    break
                else:
                    que.popleft()
    return list(answer)
