def solution(N, A):
    max_num = 0
    cur_max = 0
    lena = len(A)
    arr = [0 for _ in range(N)]
    for i in range(lena):
        a = A[i]
        if a >= 1 and a<= N :
            arr[a-1] = arr[a-1] +1 if max_num < arr[a-1]+1 else max_num +1
            cur_max = arr[a-1] if cur_max < arr[a-1] else cur_max
        elif a == N+1:
            max_num = cur_max
    for i in range(N):
        arr[i] = arr[i] if arr[i] > max_num else max_num
    return arr 
