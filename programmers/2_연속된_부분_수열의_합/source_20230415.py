def solution(sequence, k):
    
    answer = []
    result_list = []
    i = 0
    j = 1
    while True:
        if j<i or len(sequence)<j: 
            # print('brak', i, j, sum(sequence[i:j]))
            break
        if k > sum(sequence[i:j]):
            # print('j++', i, j, sum(sequence[i:j]))
            j+=1
            continue
        if k < sum(sequence[i:j]):
            # print('i++', i, j, sum(sequence[i:j]))
            i+=1
            continue
        result_list.append([i,j-1,j-i])
        i+=1
        j+=1
    result_list = sorted(result_list, key=lambda x:(x[2], x[0]))
    if len(result_list) == 0 :
        return [0,0]
    else :
        return [result_list[0][0],result_list[0][1]]
