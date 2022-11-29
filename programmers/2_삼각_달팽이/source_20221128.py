def solution(n):
    answer = list()
    front_list = [ list() for _ in range(n) ]
    back_list = [ list() for _ in range(n) ]
    #print(front_list)
    
    k = 1
    i = 0
    num = n
    row = 0
    while True:
        if num <=0 : break
        for i in range(row,num+row):
            front_list[i].append(k)
            k += 1
        num -= 1
        if num <=0 : break
        for j in range(num):
            front_list[i].append(k)
            k += 1
        num -= 1
        if num <=0 : break
        #print('?')
        for j in range(i-1, i-num-1, -1):
            #print('??')
            back_list[j].append(k)
            k += 1
        num -= 1
        i+=1
        row +=2
    for i in range(n):
        answer.extend(front_list[i])
        answer.extend(back_list[i][::-1])
    #print(front_list)
    #print(back_list)
    return answer
