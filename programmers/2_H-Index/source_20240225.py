def solution(citations):
    citations.sort()
    # print(citations)
    n = len(citations)
    h = 0
    i = 0
    answer = 0

    for h in range(1,n+1):
        print(citations[i], h, answer)
        while True:
            if i>=n-1: break
            if citations[i] < h:
                i+=1
            else:
                break
        if n-i >= h and i <= h:
            answer = h
    return answer
