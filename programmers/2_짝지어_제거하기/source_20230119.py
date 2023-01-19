def solution(s):
    answer = []
    arr = list(s)
    for alpha in arr:
        if len(answer) == 0 :
            answer.append(alpha)
            continue
        if answer[-1] == alpha:
            answer.pop()
            continue
        answer.append(alpha)
    return 1 if len(answer)==0 else 0
