def solution(begin, end):
    # arr = [1 for _ in range(1, end+1)]
    # arr[0] = 0
    arr = []
    #have_to = (int)(end ** (1/2) //1)+1
    for j in range(begin, end+1):
        k = int(j !=1)
        for i in range(2, int(j**0.5)+1):
            if k == 0 : continue
            if j%i == 0 and j//i <= 10000000:
                #and j>=i and j%i == 0:
                k=j//i
                break
        arr.append(k)
       # print(i)
    #print(arr)
    return arr
