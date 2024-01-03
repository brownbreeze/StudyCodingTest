def solution(a, b, n):
    answer = 0
    nmg = n
    while True:
        if nmg < a:
            break
        t = (nmg // a)*b
        answer += t
        nmg = nmg%a
        nmg += t
        # print(answer)
    return answer
