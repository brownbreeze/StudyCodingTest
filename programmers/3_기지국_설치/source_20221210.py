def solution(n, stations, w):
    answer = 0
    apart_arr = [0 for _ in range(n)]
    for i in range(len(stations)):
        pos = stations[i]-1
        for v in range(w+1):
            if pos-v in range(0,n):
                apart_arr[pos-v] = 1
            if pos+v in range(0,n):
                apart_arr[pos+v] = 1            
    print(apart_arr)    
    for i in range(w,n-w):
        if apart_arr[i]==1: continue
        answer += 1
        for v in range(w+1):
            if i+v in range(0,n):
                apart_arr[i+v] = 1    
    return answer
