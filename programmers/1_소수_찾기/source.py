def solution(n):
    answer = 0
    flag = [1 for _ in range(1000001)]
    flag[0]=0
    flag[1]=0
    flag[2]=1
    max_n = int(n//2)
    for i in range(2,max_n+1):
        # print('i',i)
        j = i
        while True:
            if j > n:
                break
            j += i
            if j > 1000000: break
            flag[j] = 0
            # print('j',j)
        # print(i)
    # print(flag[:n+1])
    return sum(flag[:n+1])
