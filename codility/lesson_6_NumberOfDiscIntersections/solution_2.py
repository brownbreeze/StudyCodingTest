def solution(A):
    cnt = 0
    len_a = len(A)
    array = [[] for _ in range(len_a)]
    for i in range(len_a):
        array[i] = [i - A[i],i + A[i]]
    array.sort(key=lambda x:(x[0],x[1]))
    
    for i in range(len_a):
        for j in range(i+1, len_a):
            if cnt > 10000000: 
                return -1 
            if array[j][0] > array[i][1] :
                break; 
            if array[j][0] >= array[i][0] and array[j][0] <= array[i][1]: 
                cnt +=1 
    return cnt
