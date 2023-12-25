def solution(keymap, targets):
    answer = []
    pos = [101 for _ in range(26)]
    for m in keymap:
        i = 0
        for a in m:
            pos[ord(a)-65] = min(pos[ord(a)-65],i)
            i+=1
    for target in targets:
        s = 0
        for a in target:
            t = pos[ord(a)-65]
            if t == 101:
                answer.append(-1)
                break
            s += t+1
        else:
            answer.append(s)
    return answer
