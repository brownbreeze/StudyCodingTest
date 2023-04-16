def solution(book_time):
    answer = 0
    book_time.sort(key=lambda x:(x[0], x[1]))
    #print(book_time)
    boo_time_number = []
    for bt in book_time:
        in_time = [int(x) for x in bt[0].split(":")]
        out_time = [int(x) for x in bt[1].split(":")]
        boo_time_number.append([in_time[0]*60 + in_time[1],out_time[0]*60 + out_time[1]] )
    stack = []
    for it,ot in boo_time_number:
        # print(it,ot)
        if len(stack)==0:
            stack.append(ot+10)
            continue
        data = [[i,it-stack[i]] for i in range(len(stack)) if stack[i] <= it ]
        if len(data)==0:
            stack.append(ot+10)
            continue
        data.sort(key=lambda x : x[1])
#        print('data:', data)
        stack[data[0][0]] = ot+10
        
    return len(stack)

