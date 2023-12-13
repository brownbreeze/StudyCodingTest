def solution(name, yearning, photo):
    answer = []
    dc = dict()
    n_name = len(name)
    for i in range(n_name):
        dc[name[i]] = yearning[i]
    
    for missing in photo:
        num = 0
        for name in missing:
            if name in dc:
                num+= dc[name]
        answer.append(num)
    return answer
