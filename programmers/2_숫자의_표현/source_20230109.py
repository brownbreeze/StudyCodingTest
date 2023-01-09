def solution(n):
    answer = 0
    arr = []
    for i in range(1, n):
        num = 0
        for j in range(i, n):
            num += j
            # print(i, j, num)
            if num == n : 
                answer += 1
            elif num > n:
                break
    return answer+1
