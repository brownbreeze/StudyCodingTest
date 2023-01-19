def solution(s):
    answer = -1
    pos = 0
    arr = list(s)
    flag = 0
    while True:
        if pos+1 >= len(arr):
            if flag == 0 : break 
            flag = 0
            pos = 0
        if arr[pos]==arr[pos+1]:
            # print(f'arr:{arr}, pos:{pos}')
            arr.pop(pos)
            arr.pop(pos)
            flag = 1
        else:
            pos += 1
        if len(arr) == 0 or len(arr) == 1: 
            break
    return 1 if len(arr)==0 else 0
