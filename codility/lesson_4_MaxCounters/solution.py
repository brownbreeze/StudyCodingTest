def solution(N, A):
    max_num = 1
    lena = len(A)
    arr = [0 for _ in range(N)]
    for i in range(lena):
        a = A[i]
        if a >= 1 and a<= N :
            arr[a-1] += 1
        elif a == N+1:
            max_num = max(arr)
            arr = [max_num for _ in range(N)]
    return arr 
