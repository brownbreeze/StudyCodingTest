def solution(food):
    answer = ''
    l = len(food)
    li = []
    for i in range(1,l):
        li.append(food[i]//2)
    for i in range(len(li)):
        for j in range(li[i]):
            answer += str(i+1)
    return answer + '0' + answer[::-1]
