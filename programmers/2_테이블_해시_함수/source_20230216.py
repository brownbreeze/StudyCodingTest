def solution(data, col, row_begin, row_end):
    answer = -1
    data.sort(key=lambda x:(x[col-1],-x[0]))
    s_i = 0 
    temp = -1
    for i in range(row_begin-1, row_end):            
        s_i = 0 
        for d in data[i]:
            s_i += d%(i+1)
        if temp == -1:
            temp = s_i
        else:
            temp = temp^s_i
    return temp
