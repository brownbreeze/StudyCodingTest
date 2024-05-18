import math
def solution(n, stations, w):
    answer = 0
    if n == 0: return 0
    i = 0 
    wl = w*2+1
    # arr = list()

    for station in stations:
        s = station - w
        e = station + w 
        l = s-1-i
        answer += math.ceil(l/wl)
        # arr.append([i,l])
        # print(math.ceil(l/wl))
        i = e
    else:
        if i < n:        
            l = l-1
            answer += math.ceil(l/wl)
            # arr.append([i,l])
            # print(math.ceil(l/wl))
    # print(arr)

    return answer
