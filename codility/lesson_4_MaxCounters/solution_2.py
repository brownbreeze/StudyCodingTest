def solution(N, A):
    max_num = 0
    lena = len(A)
    arr = [0 for _ in range(N)]
    for i in range(lena):
        a = A[i]
        if a >= 1 and a<= N :
            arr[a-1] = arr[a-1] +1 if max_num <= arr[a-1]+1 else max_num + 1
        elif a == N+1:
            max_num = max(arr)
    for i in range(N):
        arr[i] = max(arr[i], max_num)
    return arr 
