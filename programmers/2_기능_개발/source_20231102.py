import math
def solution(progresses, speeds):
    answer = []
    len_total = len(progresses)
    days = 0
    for i in range(len_total):
        progress = progresses[i]
        speed = speeds[i]
        if progress + days * speed < 100:
            days = days + math.ceil((100-progress)/speed)
            answer.append(1)
        else : 
            answer[-1] +=1
    return answer
