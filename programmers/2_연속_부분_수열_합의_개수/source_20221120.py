def solution(elements):
    gp = set()
    for i in range(len(elements)):
        num = i
        temp_sum = 0
        for _ in range(len(elements)):
            temp_sum = temp_sum + elements[num]
            gp.add(temp_sum)
            num = (num+1)%len(elements)   
    return len(gp)

