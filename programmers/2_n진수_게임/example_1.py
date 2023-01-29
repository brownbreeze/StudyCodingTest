big = ["A","B","C","D","E","F"]
def solution(n, t, m, p):
    a="0"
    i=0
    #for i in range(t*m):
    while True:
        if len(a)>=t*m:
            break
        b=""
        j=i
        while (j):
            if j%n>9:
                b=big[j%n-10]+b
            else:
                b=str(j%n)+b
            j=j//n
        a=a+b
        i=i+1
    answer = a[p-1::m][:t]
    return answer

