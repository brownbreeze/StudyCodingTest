def check(arr, fr, fc, width, result):
    num = arr[fr][fc]
    if width == 1:
        result[num] += 1
        return result
    flag = True
    for r in range(fr, fr+width):
        for c in range(fc, fc+width):
            if arr[r][c] != num: 
                flag = False
                break
        if flag == False : break
    if flag is False and width > 1:
        result = check(arr, fr, fc, width//2, result)
        result = check(arr, fr+width//2, fc, width//2, result)
        result = check(arr, fr, fc+width//2, width//2, result)
        result = check(arr, fr+width//2, fc+width//2, width//2, result)
    else:
        result[num] += 1
    return result

def solution(arr):
    width = len(arr)
    result = [0,0]
    result=check(arr, 0,0, width, result)
    return result
