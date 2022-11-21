def solution(n, left, right):
    answer = []
    for j in range(int(left/n), n):
        for i in range(n):
            if j*n+i < left : continue
            if j*n+i > right: return answer
            answer.append(j+1 if i < j else i+1)
    return answer
