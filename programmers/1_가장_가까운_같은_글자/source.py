def solution(s):
    answer = []
    i = 0
    alpa_pos = [-1 for _ in range(26)]
    for ch in s:
        p = ord(ch)-97
        if alpa_pos[p] == -1:
            answer.append(-1)
        else:
            answer.append(i-alpa_pos[p])
        alpa_pos[p] = i
        i+=1
    return answer
