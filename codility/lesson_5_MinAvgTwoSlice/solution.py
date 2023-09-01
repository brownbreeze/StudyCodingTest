def solution(A):
    lena = len(A)
    mintemp = 100000
    rst = 0
    for i in range(0,lena-1):
        for j in range(0, lena-i-1):
            if mintemp > sum(A[j:i+j+2])/(i+2):
                mintemp = sum(A[j:i+j+2])/(i+2)
                rst = j
    return rst

        # print(mintemp)
