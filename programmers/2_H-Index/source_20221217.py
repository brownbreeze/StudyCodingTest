def solution(citations):
    citations.sort()
    answer, last_cnt = 0, citations[-1] 
    for i in range(1,last_cnt):
        iy_cnt = sum([1 for t in citations if t >= i])
        if i <= iy_cnt and answer < iy_cnt:
            answer = i
        elif i > iy_cnt:
            break
    return answer
