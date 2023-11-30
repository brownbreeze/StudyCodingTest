def solution(arr1, arr2):
    answer = arr1.copy()
    len_arr = len(arr1)
    pos = 0
    for ar1, ar2 in zip(arr1,arr2):
        len_ar = len(ar1)
        for i in range(len_ar):
            answer[pos][i] = ar1[i]+ar2[i]
        pos +=1
            
    return answer
