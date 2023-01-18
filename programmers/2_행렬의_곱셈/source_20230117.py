def solution(arr1, arr2):
    answer = [[]]
    arr1_col_len = len(arr1[0])
    arr1_row_len = len(arr1)
    arr2_col_len = len(arr2[0])
    #print(arr1_row_len,arr2_col_len)
    for r in range(arr1_row_len):
        for c in  range(arr2_col_len):
            temp = [arr1[r][x] * arr2[x][c] for x in range(arr1_col_len)]
            answer[r].append(sum(temp))
        answer.append([])
    answer.pop()
    return answer
