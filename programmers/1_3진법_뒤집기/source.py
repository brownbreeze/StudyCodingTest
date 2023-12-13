def solution(n):
    answer = 0
    i = n
    li = []
    while True:
        if i<3:
            li.append(i)
            break
        li.append(i%3)
        i = i//3
    # print(li)
    li.reverse()
    # print(li)
    a = 0
    for i in li:
        answer+=i*pow(3,a)
        a+=1
    return answer
