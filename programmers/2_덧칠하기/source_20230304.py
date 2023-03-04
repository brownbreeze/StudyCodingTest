def solution(n, m, section):
    answer = 0
    if m==1:
        return len(section)
    cur = 1
    idx = -1
    ok = 0
    while True:
        idx +=1
        if len(section) <=idx: break
        if ok >= section[idx]: continue
        ok = section[idx]+m-1
        answer +=1
    return answer
