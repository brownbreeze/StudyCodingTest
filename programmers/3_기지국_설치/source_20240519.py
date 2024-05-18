def solution(n, stations, w):
    answer = 0
    # apart_arr = [0 for _ in range(n+1)]
    if n == 0 : 
        return 0
    
    # aprt_arr setting 
    j = 0 
    # for i in range(n):
    #     if i in range(stations[j]-w,stations[j]+w+1):
    #         apart_arr[i] = 1
    #     if stations[j]-1+w<i:
    #         j+=1
    #     if j >= len(stations):
    #         break 
    
    i = 0
    c = 0
    while True:
        if i > n : break 
        # if apart_arr[i] == 1:
        #     i+=1
        #     continue     
        c += 1
        i+=1
        # i += w*2+1
        # if i > n:
        #     return c
    return c
