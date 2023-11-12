def solution(lines):
    answer = 0
    li = [0 for _ in range(202)]
    for line in lines:
        for j in range(line[0], line[1]):
            li[j+100] +=1
    
    for l in li:
        if l > 1:
            answer +=1 
    return answer
