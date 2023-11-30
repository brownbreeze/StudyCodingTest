def solution(arr):
    min_n = min(arr)
    arr.remove(min_n)
    if len(arr) ==0 : 
        return [-1]
    return arr
