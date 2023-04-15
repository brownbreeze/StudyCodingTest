def solution(sequence, k):
    
    answer = []
    result_list = []
    i = 0
    j = 0
    total = sequence[0]
    while True:
        if j<i or len(sequence) < j: 
            # print('brak', i, j, total)
            break
        if k > total:
            # print('j++', i, j, total)
            j+=1
            if j >= len(sequence): 
                # print('err')
                break
            total += sequence[j]
            continue
        if k < total:
            # print('i++', i, j, total)
            total -= sequence[i]
            i+=1
            continue
        # print('correct', i, j, total)
        result_list.append([i,j,j-i])
        j+=1
        if j >= len(sequence): 
            # print('err')
            break
        total += sequence[j]
        total -= sequence[i]
        i+=1
    # print(result_list)
    result_list = sorted(result_list, key=lambda x:(x[2], x[0]))
    if len(result_list) == 0 :
        return [0,0]
    else :
        return [result_list[0][0],result_list[0][1]]
