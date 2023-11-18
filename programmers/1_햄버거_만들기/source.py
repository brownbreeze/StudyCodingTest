def solution(ingredient):
    answer = 0
    arr = []
    i_len = len(ingredient)
    for i in range(i_len):
        arr.append(ingredient[i])
        if len(arr) < 4:
            continue
        if arr[-1] != 1: continue
        if arr[-4] == 1 and arr[-3]==2 and arr[-2] == 3 and arr[-1] == 1:
            arr.pop()
            arr.pop()
            arr.pop()
            arr.pop()
            answer += 1
    return answer
