def solution(A):
    lena = len(A)
    mintemp = 100000
    rst = 0

    for i in range(0,2):
        for j in range(0, lena-i-1):
            temp = sum(A[j:i+j+2])/(i+2)
            if mintemp > temp:
                mintemp = temp
                rst = j
    return rst

